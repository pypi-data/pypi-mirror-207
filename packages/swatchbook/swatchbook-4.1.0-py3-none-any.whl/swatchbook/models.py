import re

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.models import Orderable
from wagtail.admin.panels import InlinePanel, FieldRowPanel

from django_auxiliaries.validators import python_identifier_validator, css_compatible_identifier_validator

from wagtail_block_model_field.fields import BlockModelField

from wagtail_attachments.models.mixins import StorageMixin, AttachableMixin
from wagtail_attachments.models.attachments import create_model_attachment_class
from wagtail_attachments.panels import AttachmentsPanel

from .blocks import ResponsiveColourBlock, ResponsiveColourValue, \
    ColourBlock, ColourBlockValue, ConditionalColourBlock, define_css_color, ConditionalVariableBlock

from .apps import get_app_label

APP_LABEL = get_app_label()


@register_snippet
class MediaQuery(models.Model):

    class Meta:
        verbose_name = "Media Query"
        verbose_name_plural = "Media Queries"
        constraints = [
            models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    active = models.BooleanField(default=True)
    identifier = models.CharField(max_length=128, default='', validators=[python_identifier_validator])
    definition = models.TextField(default='all')
    priority = models.IntegerField(default='0')

    panels = [
        FieldPanel('active'),
        FieldPanel('identifier'),
        FieldPanel('definition'),
        FieldPanel('priority'),
    ]

    def save(self, **kwargs):
        super(MediaQuery, self).save(**kwargs)

        from .colour_stylesheet import update_colour_stylesheet_file

        update_colour_stylesheet_file()

    def __str__(self):
        return self.identifier + (" [{:d}]".format(self.priority) if self.priority else "") # noqa


@register_snippet
class Colour(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    PREFIX = APP_LABEL + '-colour'

    identifier = models.CharField(max_length=128, default='', validators=[css_compatible_identifier_validator])

    definition = BlockModelField(ResponsiveColourBlock(required=True), ResponsiveColourValue)

    panels = [
        FieldPanel('identifier'),
        FieldPanel('definition', classname="block-model-field"),
    ]

    def save(self, **kwargs):
        super(Colour, self).save(**kwargs)

        from .colour_stylesheet import update_colour_stylesheet_file

        update_colour_stylesheet_file()
        update_colour_stylesheet_file(file_name='admin_colours.css', prefix=self.PREFIX)

    def __str__(self):

        variations = ""

        if len(self.definition['conditionals']): # noqa
            variations = " [{:d} variation(s)]".format(len(self.definition['conditionals'])) # noqa

        return mark_safe(('<span class="swatchbook-listing-colour-swatch-background"></span>' +
                          '<span class="swatchbook-listing-colour-swatch" style="background-color: var(--{})"></span>' +
                          '{}{}').format(
                             self.identifier if not self.PREFIX else self.PREFIX + '-' + self.identifier,
                             self.identifier, variations))

"""
@register_snippet
class ColourAlias(models.Model):

    class Meta:
        verbose_name = "Colour Alias"
        verbose_name_plural = "Colour Aliases"

        constraints = [
            models.UniqueConstraint(fields=['alias'], name='unique_%(app_label)s_%(class)s.alias')
        ]

    alias = models.CharField(max_length=128, default='', validators=[css_compatible_identifier_validator])
    colour = models.ForeignKey('Colour', related_name="aliases", on_delete=models.SET_NULL, blank=True, null=True)

    panels = [
        FieldRowPanel([
            FieldPanel('alias'),
            FieldPanel('colour')
        ])
    ]

    def save(self, **kwargs):
        super(ColourAlias, self).save(**kwargs)

        from .colour_stylesheet import update_colour_stylesheet_file

        update_colour_stylesheet_file()

    def __str__(self):
        return "{} -> {}".format(self.alias, self.colour.identifier if self.colour else "[undefined]") # noqa
"""


class FontFace(StorageMixin, AttachableMixin, Orderable, ClusterableModel):

    class Meta:
        verbose_name = "Font Face"
        verbose_name_plural = "Font Faces"

    storage_root = "fonts"

    family = ParentalKey('FontFamily', related_name="faces", on_delete=models.CASCADE, blank=False)

    style = models.CharField(max_length=128, default='normal')
    weight = models.CharField(max_length=128, default='400')

    panels = [
        FieldPanel('style'),
        FieldPanel('weight'),
        AttachmentsPanel()
    ]

    def attachment_saved(self, attachment):

        pass

    def attachment_deleted(self, attachment):

        pass


FontFaceAttachment = create_model_attachment_class(FontFace)


@register_snippet
class FontFamily(ClusterableModel):

    class Meta:
        verbose_name = "Font Family"
        verbose_name_plural = "Font Families"

        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_%(app_label)s_%(class)s.name')
        ]

    name = models.CharField(max_length=128, default='', validators=[css_compatible_identifier_validator])

    panels = [
        FieldPanel('name'),
        InlinePanel('faces', label="Font Faces", min_num=0, max_num=None),
    ]

    def save(self, **kwargs):
        super(FontFamily, self).save(**kwargs)

        from .font_stylesheet import update_font_stylesheet_file

        update_font_stylesheet_file()

    def __str__(self):
        return self.name + (" [{:d} face(s)]".format(self.faces.count()) if self.faces.count() > 0 else "") # noqa


@register_snippet
class FontAlias(models.Model):

    class Meta:
        verbose_name = "Font Alias"
        verbose_name_plural = "Font Aliases"

        constraints = [
            models.UniqueConstraint(fields=['alias'], name='unique_%(app_label)s_%(class)s.alias')
        ]

    alias = models.CharField(max_length=128, default='', validators=[css_compatible_identifier_validator])
    family = models.ForeignKey('FontFamily', related_name="aliases", on_delete=models.SET_NULL, blank=True, null=True)

    panels = [
        FieldRowPanel([
            FieldPanel('alias'),
            FieldPanel('family')
        ])
    ]

    def save(self, **kwargs):
        super(FontAlias, self).save(**kwargs)

        from .font_stylesheet import update_font_stylesheet_file

        update_font_stylesheet_file()

    def __str__(self):
        return "{} -> {}".format(self.alias, self.family.name if self.family else "[undefined]")


@register_snippet
class StylesheetVariable(models.Model):

    class Meta:
        verbose_name = 'Stylesheet Variable'
        verbose_name_plural = 'Stylesheet Variables'

        constraints = [
            models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    identifier = models.CharField(max_length=128, default='', validators=[css_compatible_identifier_validator])

    definition = models.TextField(default='')

    conditional_definitions = StreamField([('conditional_definition',
                                            ConditionalVariableBlock())],
                                          use_json_field=True,
                                          min_num=0,
                                          max_num=None,
                                          blank=True,
                                          null=True)

    panels = [
        FieldPanel('identifier'),
        FieldPanel('definition', classname="block-model-field"),
        FieldPanel('conditional_definitions', classname="stream-field")
    ]

    def save(self, **kwargs):
        super(StylesheetVariable, self).save(**kwargs)

        from .variable_stylesheet import update_variable_stylesheet_file
        update_variable_stylesheet_file()

    def __str__(self):

        if len(self.conditional_definitions): # noqa
            variations = " [{:d} variation(s)]".format(len(self.conditional_definitions)) # noqa
        else:
            variations = ""

        return "{} -> {}{}".format(self.identifier, self.definition, variations)