from django.db import models as django_models
from django.template.loader import render_to_string
from django.core.exceptions import SuspiciousOperation, ValidationError
from django.core.files.utils import validate_file_name as validate_file_name_impl

from django_auxiliaries.validators import python_identifier_validator

from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, FieldRowPanel

from wagtail_block_model_field.fields import BlockModelField
from wagtail_dynamic_stream_block.blocks import DynamicStreamBlock, DynamicStreamValue

from .apps import get_app_label


__all__ = ['Morsel', 'MorselAlias', 'lookup_morsel']

APP_LABEL = get_app_label()


def validate_file_name(file_name):

    try:
        validate_file_name_impl(file_name, allow_relative_path=True)
    except SuspiciousOperation:
        raise ValidationError("File names must start with a forward slash and must not contain any " +
                              "parent directory components.")


@register_snippet
class Morsel(django_models.Model):

    class Meta:

        verbose_name = 'Morsel'
        verbose_name_plural = 'Morsels'
        constraints = [
            django_models.UniqueConstraint(fields=['identifier'],
                                           name='unique_%(app_label)s_%(class)s.identifier')
        ]

    identifier = django_models.CharField(max_length=128, validators=[python_identifier_validator])
    name = django_models.CharField(max_length=128)

    template = django_models.CharField(max_length=128, verbose_name="Template Path", blank=True, null=True,
                                       validators=(validate_file_name,))

    content = BlockModelField(DynamicStreamBlock(child_blocks_function_name=APP_LABEL + ".blocks.morsel_block_choices",
                                                 template=APP_LABEL + "/blocks/morsel_content_stream.html"),
                              value_class=DynamicStreamValue)

    panels = [
        FieldRowPanel([
            FieldPanel('identifier'),
            FieldPanel('name')
        ]),
        FieldPanel('template'),
        FieldPanel('content')
    ]

    @property
    def applicable_template(self):
        result = self.template if self.template else "/" + APP_LABEL + "/base.html"

        if result.startswith("/"):
            result = result[1:]

        return result

    # noinspection PyMethodMayBeStatic
    def render(self, request, page, context=None, **kwargs):

        new_context = dict(context) if context else {}

        new_context.update({
            'page': page,
            'request': request,
            'morsel': self,
            'options': kwargs
        })

        return render_to_string(self.applicable_template, context=new_context, request=request)

    def __str__(self):
        return '{}: {}'.format(self.identifier, self.name)


@register_snippet
class MorselAlias(django_models.Model):

    class Meta:
        verbose_name = "Morsel Alias"
        verbose_name_plural = "Morsel Aliases"

        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    identifier = django_models.CharField(max_length=128, default='', validators=[python_identifier_validator])
    morsel = django_models.ForeignKey('Morsel', related_name="aliases", on_delete=django_models.SET_NULL,
                                     blank=True, null=True)

    panels = [
        FieldRowPanel([
            FieldPanel('identifier'),
            FieldPanel('morsel')
        ])
    ]

    def __str__(self):
        return "{} -> {}".format(self.identifier, self.morsel.name if self.morsel else "[undefined]")


def lookup_morsel(identifier):

    morsel = None

    try:
        alias = MorselAlias.objects.get(identifier=identifier)
        morsel = alias.morsel

    except MorselAlias.DoesNotExist:
        pass

    if morsel is None:
        try:
            morsel = Morsel.objects.get(identifier=identifier)
        except Morsel.DoesNotExist:
            pass

    return morsel
