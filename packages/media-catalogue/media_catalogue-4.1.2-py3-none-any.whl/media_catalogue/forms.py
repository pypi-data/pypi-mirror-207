from django import forms
from django.conf import settings
from django.forms.models import modelform_factory
from django.utils.text import capfirst
from django.utils.translation import gettext as _

from wagtail.admin import widgets
from wagtail.admin.forms.collections import (
    BaseCollectionMemberForm, CollectionChoiceField, collection_member_permission_formset_factory)
from wagtail.models import Collection

from media_catalogue.form_fields import MediaItemField
from media_catalogue.formats import get_media_item_formats
from media_catalogue.models.media_items import MediaItem
from media_catalogue.models.permissions import permission_policy as media_items_permission_policy

__all__ = ['get_media_item_base_form', 'get_media_item_form', 'get_media_item_multi_form', 'MediaItemInsertionForm']


# Callback to allow us to override the default form field for the image file field and collection field.
def formfield_for_dbfield(db_field, **kwargs):
    # Check if this is the file field
    # if db_field.name == 'file':
    #    return MediaItemField(label=capfirst(db_field.verbose_name), **kwargs)
    if db_field.name == 'collection':
        return CollectionChoiceField(label=_("Collection"), queryset=Collection.objects.all(), empty_label=None, **kwargs)

    # For all other fields, just call its formfield() method.
    return db_field.formfield(**kwargs)


class BaseMediaItemForm(BaseCollectionMemberForm):

    permission_policy = media_items_permission_policy

    class Meta:

        widgets = {
            'tags': widgets.AdminTagWidget,
            # 'file': forms.FileInput(),
            # 'focal_point_x': forms.HiddenInput(attrs={'class': 'focal_point_x'}),
        }


def get_media_item_base_form():
    base_form_override = getattr(settings, "MEDIA_CATALOGUE_MEDIA_ITEM_FORM_BASE", "")
    if base_form_override:
        from django.utils.module_loading import import_string
        base_form = import_string(base_form_override)
    else:
        base_form = BaseMediaItemForm
    return base_form


def get_media_item_form(model_class):
    fields = model_class.admin_form_fields
    if 'collection' not in fields:
        # force addition of the 'collection' field, because leaving it out can
        # cause dubious results when multiple collections exist (e.g adding the
        # document to the root collection where the user may not have permission) -
        # and when only one collection exists, it will get hidden anyway.
        fields = list(fields) + ['collection']

    return modelform_factory(
        model_class,
        form=get_media_item_base_form(),
        fields=fields,
        formfield_callback=formfield_for_dbfield,
    )


def get_media_item_multi_form(model_class):
    # edit form for use within the multiple uploader
    MediaItemForm = get_media_item_form(model_class)

    # Make a new form with the file and focal point fields excluded
    class MediaItemEditForm(MediaItemForm):
        class Meta(MediaItemForm.Meta):
            model = model_class
            exclude = (
                # 'file',
                # 'focal_point_x',
            )

    return MediaItemEditForm


class MediaItemInsertionForm(forms.Form):
    """
    Form for selecting parameters of the image (e.g. format) prior to insertion
    into a rich text area
    """
    format = forms.ChoiceField(
        label=_("Format"),
        choices=[(format.name, format.label) for format in get_media_item_formats()],
        widget=forms.RadioSelect
    )
    media_item_is_decorative = forms.BooleanField(required=False, label=_("MediaItem is decorative"))
    alt_text = forms.CharField(required=False, label=_("Alt text"))

    def clean_alt_text(self):
        alt_text = self.cleaned_data['alt_text']
        media_item_is_decorative = self.cleaned_data['media_item_is_decorative']

        # Empty the alt text value if the image is set to be decorative
        if media_item_is_decorative:
            return ''
        else:
            # Alt text is required if image is not decorative.
            if not alt_text:
                msg = _("Please add some alt text for your media item or mark it as decorative")
                self.add_error('alt_text', msg)
        return alt_text


class URLGeneratorForm(forms.Form):
    filter_method = forms.ChoiceField(
        label=_("Filter"),
        choices=(
            ('original', _("Original size")),
            ('width', _("Resize to width")),
            ('height', _("Resize to height")),
            ('min', _("Resize to min")),
            ('max', _("Resize to max")),
            ('fill', _("Resize to fill")),
        ),
    )

    width = forms.IntegerField(label=_("Width"), min_value=0)
    height = forms.IntegerField(label=_("Height"), min_value=0)
    closeness = forms.IntegerField(label=_("Closeness"), min_value=0, initial=0)


GroupImagePermissionFormSet = collection_member_permission_formset_factory(
    MediaItem,
    [
        ('add_media_item', _("Add"), _("Add/edit media item you own")),
        ('change_media_item', _("Edit"), _("Edit any media item")),
        ('choose_media_item', _("Choose"), _("Select media items in choosers")),
    ],
    'media_catalogue/permissions/includes/media_item_permissions_formset.html'
)
