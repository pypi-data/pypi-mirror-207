import collections
import importlib
import sys

from wagtail import blocks
from wagtail.blocks.stream_block import StreamBlockAdapter
from wagtail.telepath import register

from wagtail_switch_block import SwitchBlock
from wagtail_switch_block.block_registry import BlockRegistry
from wagtail_switch_block.function_specifier import FunctionSpecifier

from wagtail_dynamic_choice.blocks import AlternateSnippetChooserBlock

from model_porter.support_mixin import ModelPorterSupportMixin

from .apps import get_app_label

__all__ = ['MorselBlock', 'register_morsel_block', 'morsel_block_choices' # noqa
          ]

mod = sys.modules[__name__]

APP_LABEL = get_app_label()


class MorselBlock(blocks.StructBlock):

    class Meta:
        icon = 'link'
        template = APP_LABEL + '/blocks/morsel_block.html'
        default = {}

    identifier = SwitchBlock(local_blocks=[
        ('alias', AlternateSnippetChooserBlock(APP_LABEL + ".morselalias", use_identifier_as_value=True)),
        ('morsel', AlternateSnippetChooserBlock(APP_LABEL + ".morsel", use_identifier_as_value=True))
    ])

    # noinspection PyMethodMayBeStatic
    def lookup_morsel(self, value):

        from .models import lookup_morsel
        return lookup_morsel(value['identifier'])

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class MorselBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):

        block_kwargs = dict(entry.block_kwargs)
        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


MORSEL_BLOCK_REGISTRY = MorselBlockRegistry()
MORSEL_BLOCK_REGISTRY.define_procedures_in_caller_module("morsel")
