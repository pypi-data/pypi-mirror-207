import collections
import sys

from wagtail import blocks
from wagtail.blocks.stream_block import StreamBlockAdapter
from wagtail.telepath import register

from .function_specifier import FunctionSpecifier
from .apps import get_app_label


__all__ = ['DynamicStreamBlock', 'DynamicStreamValue', 'update_dynamic_stream_blocks']

mod = sys.modules[__name__]

APP_LABEL = get_app_label()

DYNAMIC_STREAM_BLOCK_REGISTRY = dict()

blocks_in_registry_were_updated = False


def register_dynamic_stream_block(block):
    DYNAMIC_STREAM_BLOCK_REGISTRY[id(block)] = block


def update_dynamic_stream_blocks():

    global blocks_in_registry_were_updated

    if blocks_in_registry_were_updated:
        return

    blocks_in_registry_were_updated = True

    traversed = set()

    while True:

        remaining = traversed.symmetric_difference(DYNAMIC_STREAM_BLOCK_REGISTRY.keys())

        if not remaining:
            break

        for key in remaining:
            block = DYNAMIC_STREAM_BLOCK_REGISTRY[key]
            block.update_child_blocks()

        traversed.update(remaining)


try:

    from model_porter.support_mixin import ModelPorterSupportMixin

except (ModuleNotFoundError, ImportError):

    class ModelPorterSupportMixin:
        def from_repository(self, value, context):
            return value

DynamicStreamValue = blocks.StreamValue


class DynamicStreamBlock(ModelPorterSupportMixin, blocks.StreamBlock):

    def __init__(self, *, child_blocks_function_name, **kwargs):

        if "local_blocks" in kwargs:
            del kwargs["local_blocks"]

        self.child_blocks_function = FunctionSpecifier(function_path=child_blocks_function_name)

        super().__init__(**kwargs)

        register_dynamic_stream_block(self)

        self.update_child_blocks()

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def update_child_blocks(self):
        self.child_blocks = collections.OrderedDict(self.base_blocks)
        self.child_blocks.update(collections.OrderedDict(self.child_blocks_function(switch_block=self)))

    # noinspection PyMethodMayBeStatic
    def from_repository(self, value, context):

        result = []

        for stream_item in value:

            block_type = stream_item["type"]
            value = stream_item["value"]

            item_block_def = self.child_blocks.get(block_type, None)

            if item_block_def is None:
                continue

            if isinstance(item_block_def, ModelPorterSupportMixin):
                value = item_block_def.from_repository(value, context)

            result.append({"type": block_type, "value": value})

        return result


register(StreamBlockAdapter(), DynamicStreamBlock)
