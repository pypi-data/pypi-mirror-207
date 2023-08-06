# Django

from collections import defaultdict
from typing import *
import warnings

from django.conf import settings
from django.db import models as django_models
from django.db.models import Q
from django.db.models import (ForeignKey, CharField, EmailField, DecimalField, TextField)

from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import BaseIterable, ModelIterable
from django.apps import apps

# Wagtail

from wagtail.search.index import SearchField, Indexed
from wagtail.models import Orderable
from wagtail.fields import RichTextField

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.coreutils import camelcase_to_underscore

from django_countries.fields import CountryField

# Panels

from wagtail.admin.panels import (FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel)

from media_catalogue.blocks import MediaItemChooserBlock, MediaItemChooserBlockValue

from tour_guide.blocks import RichLinkBlock, RichLinkBlockValue

from wagtail_block_model_field.fields import BlockModelField
from wagtail_association_panel.association_panel import AssociationPanel

from wagtail_dynamic_choice.model_fields import DynamicChoiceField

# Registration Decorators

from wagtail.snippets.models import register_snippet

from .address_formats import lookup_address_format, POSTAL_ADDRESS_FORMAT_PLAIN
from .apps import get_app_label
from .blocks import * # We import blocks here so that the content block registrations are executed

__all__ = ['AddressFormat', 'Address',
           'GroupMember', 'Person', 'Organisation',
           'Group', 'GroupAssignment']

APP_LABEL = get_app_label()

DEFAULT_RICH_TEXT_EDITOR = APP_LABEL + ".shortdescription"

identifier_validator = RegexValidator("^[A-Za-z_][A-Za-z_0-9]*$",
                                      message=("A valid identifier starts with an alphanumeric letter or underscore " +
                                               "and contains only alphanumeric letters, underscores or digits."),
                                      code="invalid_identifier")


@register_snippet
class AddressFormat(django_models.Model):
    class Meta:
        verbose_name = 'Address Format'
        verbose_name_plural = 'Address Formats'

        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    @property
    def method_instance(self):
        return lookup_address_format(self.method, POSTAL_ADDRESS_FORMAT_PLAIN).function

    identifier = CharField(max_length=128, default='', validators=[identifier_validator])
    description = CharField("Description", max_length=192, blank=True)

    method = DynamicChoiceField(verbose_name="Method",
                                max_length=128,
                                choices_function_name=APP_LABEL + ".address_formats.get_address_format_choices",
                                null=False, blank=False,
                                default=APP_LABEL + ":postal")

    def __str__(self):
        return f"{self.identifier}: {self.description} [{self.method}]"


@register_snippet
class Address(Indexed, ClusterableModel):
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['town', 'postal_code', 'street', 'building_number', 'building', 'building_unit']
        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    @property
    def google_maps_url(self):
        if not self.longitude or not self.latitude:
            return ""

        return "https://www.google.co.uk/maps/search/?api=1&query={},{}".format(self.longitude, self.latitude)

    identifier = CharField(max_length=128, default='', validators=[identifier_validator],
                                         help_text="Optional organisation name, line breaks will be preserved.")

    organisation = TextField("Organisation", max_length=192, blank=True,
                             help_text="Organisation, such as \"University College London\"")

    building_unit = CharField("Building Unit", max_length=192, blank=True,
                              help_text="Unit in building, for example: \"Flat 4\", " +
                                        "\"First Floor\", \"Atrium\", \"Acute Admissions\"")

    building = CharField("Building", max_length=192, blank=True,
                         help_text="For example: Russell Square House, Maple House")

    building_number = CharField("Building Number", max_length=24, blank=False)
    street = CharField("Street", max_length=192, blank=False)
    locality = CharField("Locality", max_length=192, blank=True,
                         help_text="Useful if a street name exists more than once in the same place.")
    town = CharField("Town", max_length=192, blank=False)
    postal_code = CharField("Postal Code", max_length=32, blank=False)
    country = CountryField(default="GB", blank=False)

    longitude = DecimalField("Longitude", max_digits=9, decimal_places=6, blank=False, null=True)
    latitude = DecimalField("Latitude", max_digits=9, decimal_places=6, blank=False, null=True)

    directions = RichTextField("Directions", blank=True, null=True)

    # noinspection SpellCheckingInspection

    panels = [

        MultiFieldPanel([

            FieldPanel('identifier'),
            FieldPanel('organisation'),

            FieldRowPanel([
                FieldPanel('building_unit', classname="col6"),
                FieldPanel('building', classname="col6")
            ]),

            FieldRowPanel([
                FieldPanel('building_number', classname="col6"),
                FieldPanel('street', classname="col6")
            ]),

            FieldRowPanel([
                FieldPanel('locality', classname="col6"),
                FieldPanel('town', classname="col6"),
            ]),

            FieldRowPanel([
                FieldPanel('country', classname="col6"),
                FieldPanel('postal_code', classname="col6"),
            ]),

            FieldRowPanel([
                FieldPanel('longitude', classname="col6"),
                FieldPanel('latitude', classname="col6"),
            ]),

            FieldPanel('directions'),

        ], "Description")
    ]

    search_fields = [
        SearchField('identifier'),
        SearchField('organisation'),
        SearchField('building_unit'),
        SearchField('building'),
        SearchField('building_number'),
        SearchField('street'),
        SearchField('locality'),
        SearchField('town'),
        SearchField('postal_code'),
        SearchField('directions'),
    ]

    def __str__(self):
        return '{} {} {}\n{}\n{} [{}]'.format(self.organisation, self.building_number, self.street, self.town,
                                              self.postal_code, self.country)


class SpecificIterable(BaseIterable):
    def __iter__(self):
        """
        Identify and return all specific group members in a queryset, and return them
        in the same order, with any annotations intact.
        """

        qs = self.queryset
        annotation_aliases = qs.query.annotations.keys()
        values_qs = qs.values("pk", "content_type", *annotation_aliases)

        # Gather pages in batches to reduce peak memory usage
        for values in self._get_chunks(values_qs):

            annotations_by_pk = defaultdict(list)
            if annotation_aliases:
                # Extract annotation results keyed by pk so we can reapply to fetched pages.
                for data in values:
                    annotations_by_pk[data["pk"]] = {
                        k: v for k, v in data.items() if k in annotation_aliases
                    }

            pks_and_types = [[v["pk"], v["content_type"]] for v in values]
            pks_by_type = defaultdict(list)
            for pk, content_type in pks_and_types:
                pks_by_type[content_type].append(pk)

            # Content types are cached by ID, so this will not run any queries.
            content_types = {
                pk: ContentType.objects.get_for_id(pk) for _, pk in pks_and_types
            }

            # Get the specific instances of all members, one model class at a time.
            members_by_type = {}
            missing_pks = []

            for content_type, pks in pks_by_type.items():
                # look up model class for this content type, falling back on the original
                # model (i.e. Page) if the more specific one is missing
                model = content_types[content_type].model_class() or qs.model
                members = model.objects.filter(pk__in=pks)

                members_for_type = {member.pk: member for member in members}
                members_by_type[content_type] = members_for_type
                missing_pks.extend(pk for pk in pks if pk not in members_for_type)

            # Fetch generic pages to supplement missing items
            if missing_pks:
                generic_members = (
                    GroupMember.objects.filter(pk__in=missing_pks)
                        .select_related("content_type")
                        .in_bulk()
                )
                warnings.warn(
                    "Specific versions of the following group members could not be found. "
                    "This is most likely because a database migration has removed "
                    "the relevant table or record since the member was created:\n{}".format(
                        [
                            {"id": p.id, "title": p.title, "type": p.content_type}
                            for p in generic_members.values()
                        ]
                    ),
                    category=RuntimeWarning,
                )
            else:
                generic_members = {}

            # Yield all pages in the order they occurred in the original query.
            for pk, content_type in pks_and_types:
                try:
                    page = members_by_type[content_type][pk]
                except KeyError:
                    page = generic_members[pk]
                if annotation_aliases:
                    # Reapply annotations before returning
                    for annotation, value in annotations_by_pk.get(page.pk, {}).items():
                        setattr(page, annotation, value)
                yield page

    def _get_chunks(self, queryset) -> Iterable[Tuple[Dict[str, Any]]]:
        if not self.chunked_fetch:
            # The entire result will be stored in memory, so there is no
            # benefit to splitting the result
            yield tuple(queryset)
        else:
            # Iterate through the queryset, returning the rows in manageable
            # chunks for self.__iter__() to fetch full pages for
            current_chunk = []
            for r in queryset.iterator(self.chunk_size):
                current_chunk.append(r)
                if len(current_chunk) == self.chunk_size:
                    yield tuple(current_chunk)
                    current_chunk.clear()
            # Return any left-overs
            if current_chunk:
                yield tuple(current_chunk)


class DeferredSpecificIterable(ModelIterable):
    def __iter__(self):
        for obj in super().__iter__():
            if obj.specific_class:
                yield obj.specific_deferred
            else:
                warnings.warn(
                    "A specific version of the following group member could not be returned "
                    "because the specific group member model is not present on the active "
                    f"branch: <GroupMember id='{obj.id}' title='{obj.title}' "
                    f"type='{obj.content_type}'>",
                    category=RuntimeWarning,
                )
                yield obj


class GroupMemberQuerySet(django_models.QuerySet):

    def get(self, *args, **kwargs):

        result = super().get(*args, **kwargs)
        return result

    # noinspection PyMethodMayBeStatic
    def type_q(self, klass):
        content_types = ContentType.objects.get_for_models(*[
            model for model in apps.get_models()
            if issubclass(model, klass)
        ]).values()

        return Q(content_type__in=content_types)

    def type(self, model):
        """
        This filters the QuerySet to only contain pages that are an instance
        of the specified model (including subclasses).
        """
        return self.filter(self.type_q(model))

    def not_type(self, model):
        """
        This filters the QuerySet to not contain any pages which are an instance of the specified model.
        """
        return self.exclude(self.type_q(model))

    def specific(self, defer=False):
        clone = self._clone()
        if defer:
            clone._iterable_class = DeferredSpecificIterable
        else:
            clone._iterable_class = SpecificIterable
        return clone


GROUP_MEMBER_MODEL_CLASSES = []


def get_group_member_models():
    """
    Returns a list of all non-abstract GroupMember model classes defined in this project.
    """
    return GROUP_MEMBER_MODEL_CLASSES


def get_default_group_member_content_type():
    """
    Returns the content type to use as a default for group members whose content type
    has been deleted.
    """
    return ContentType.objects.get_for_model(GroupMember)


class GroupMemberClass(django_models.base.ModelBase):
    """Metaclass for GroupMember"""

    def __init__(cls, name, bases, dct):
        super(GroupMemberClass, cls).__init__(name, bases, dct)

        if 'template' not in dct:
            # Define a default template path derived from the app name and model name
            # noinspection PyUnresolvedReferences
            cls.template = "%s/%s.html" % (cls._meta.app_label, camelcase_to_underscore(name))

        if 'ajax_template' not in dct:
            cls.ajax_template = None

        # All group members should be creatable unless explicitly set otherwise.
        # This attribute is not inheritable.
        if 'is_creatable' not in dct:
            # noinspection PyUnresolvedReferences
            cls.is_creatable = not cls._meta.abstract

        # noinspection PyUnresolvedReferences, SpellCheckingInspection
        if not cls._meta.abstract and dct.get("__qualname__", None) != "GroupMember":
            # register this type in the list of page content types
            GROUP_MEMBER_MODEL_CLASSES.append(cls)


class BaseGroupMemberManager(django_models.Manager):
    def get_queryset(self):
        return self._queryset_class(self.model)


GroupMemberManager = BaseGroupMemberManager.from_queryset(GroupMemberQuerySet)


class GroupMember(Indexed, ClusterableModel, metaclass=GroupMemberClass):
    class Meta:
        verbose_name = 'Group Member'
        verbose_name_plural = 'Group Members'

        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    @property
    def visual(self):
        return None

    objects = GroupMemberManager()

    identifier = django_models.CharField(max_length=128, default='', validators=[identifier_validator])

    active = django_models.BooleanField(verbose_name=_('active'), default=True, editable=True)

    content_type = ForeignKey(
        'contenttypes.ContentType',
        verbose_name=_('content type'),
        related_name='group_members',
        on_delete=django_models.SET(get_default_group_member_content_type)
    )

    @cached_property
    def groups(self):
        # noinspection PyUnresolvedReferences
        groups = GroupAssignment.objects.filter(member=self.id).values_list("group")
        groups = Group.objects.filter(id__in=groups)
        return groups

    @cached_property
    def specific(self):
        """
        Return this page in its most specific subclassed form.
        """
        # the ContentType.objects manager keeps a cache, so this should potentially
        # avoid a database lookup over doing self.content_type. I think.

        # noinspection PyUnresolvedReferences
        content_type = ContentType.objects.get_for_id(self.content_type_id)
        model_class = content_type.model_class()
        if model_class is None:
            # Cannot locate a model class for this content type. This might happen
            # if the codebase and database are out of sync (e.g. the model exists
            # on a different git branch and we haven't rolled back migrations before
            # switching branches); if so, the best we can do is return the page
            # unchanged.
            return self
        elif isinstance(self, model_class):
            # self is already the an instance of the most specific class
            return self
        else:
            # noinspection PyUnresolvedReferences
            return content_type.get_object_for_this_type(id=self.id)

    #: Return the class that this page would be if instantiated in its
    #: most specific form
    @cached_property
    def specific_class(self):
        """
        Return the class that this group member would be if instantiated in its
        most specific form
        """

        # noinspection PyUnresolvedReferences
        content_type = ContentType.objects.get_for_id(self.content_type_id)
        return content_type.model_class()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # noinspection PyUnresolvedReferences
        if not self.id:
            # this model is being newly created
            # rather than retrieved from the db;
            # noinspection PyUnresolvedReferences
            if not self.content_type_id:
                # set content type to correctly represent the model class
                # that this was created as
                self.content_type = ContentType.objects.get_for_model(self)


@register_snippet
class Organisation(GroupMember):
    class Meta:
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'
        ordering = ['name']

    @property
    def visual(self):
        return self.logo

    name = CharField("Name", max_length=192, blank=False, null=False)
    abbreviation = CharField("Abbreviation", max_length=192)

    link = BlockModelField(RichLinkBlock(label="Link"), RichLinkBlockValue, blank=True, null=True)

    short_description = RichTextField("Short Description", default="", editor=DEFAULT_RICH_TEXT_EDITOR,
                                      blank=True, null=True)

    logo = BlockModelField(MediaItemChooserBlock(
        max_num_choices=1,
        label="Organisation Logo",
        required=False),
        MediaItemChooserBlockValue,
        blank=True,
        null=True)

    panels = [

        MultiFieldPanel([

            FieldRowPanel([
                FieldPanel('name'), FieldPanel('identifier')
            ]),

            FieldPanel('short_description'),
            FieldPanel('logo', classname='block-model-field')
        ], "Description"),

        FieldPanel('link', classname='block-model-field'),

        MultiFieldPanel([
            AssociationPanel('groups'),
        ], "Groups")
    ]

    search_fields = [
        SearchField('name'),
        SearchField('abbreviation'),
        SearchField('short_description'),
    ]

    def __str__(self):
        return '{} [{}]'.format(self.name, self.abbreviation)


@register_snippet
class Person(GroupMember):

    class Meta:
        abstract = False
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['family_name', 'given_names_and_initials']

    @property
    def visual(self):
        return self.portrait

    @property
    def name(self):
        return self.full_name_no_title

    @property
    def full_name(self, protected=True):
        result = '{} {}'.format(self.given_names_and_initials, self.family_name)

        # noinspection PyUnresolvedReferences
        title = self.title.strip()

        if title:
            result = title + " " + result

        if protected:
            result = protect(result)

        return result

    @property
    def full_name_no_title(self, protected=True):
        result = '{} {}'.format(self.given_names_and_initials, self.family_name)

        if protected:
            result = protect(result)

        return result

    family_name = CharField("Family Name", default="", max_length=192, blank=False)
    given_names_and_initials = CharField("Given Name(s) and Initial(s)", default="", max_length=192, blank=False)

    title = CharField("Title", default="", max_length=192, blank=True)

    email = EmailField("Email", default="", blank=True, null=True)

    user = django_models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'), related_name="person",
                                       blank=True, null=True, on_delete=django_models.SET_NULL)

    link = BlockModelField(RichLinkBlock(label="Link"), RichLinkBlockValue, blank=True, null=True)

    short_description = RichTextField("Short Description", default="", editor=DEFAULT_RICH_TEXT_EDITOR,
                                      blank=True, null=True)

    portrait = BlockModelField(MediaItemChooserBlock(
        max_num_choices=1,
        label="Portrait",
        required=False),
        MediaItemChooserBlockValue, blank=True, null=True)

    panels = [

        MultiFieldPanel([

            FieldRowPanel([
                FieldPanel('family_name'),
                FieldPanel('given_names_and_initials'),
                FieldPanel('title'),
            ]),

            FieldRowPanel([
                FieldPanel("user"),
                FieldPanel("identifier"),
            ]),

            FieldPanel("portrait", classname="block-model-field"),

        ], "Identity"),

        MultiFieldPanel([
            FieldPanel("email"),
        ], "Contact"),

        MultiFieldPanel([
            FieldPanel("short_description"),
        ], "Description"),

        FieldPanel('link', classname="block-model-field"),

        MultiFieldPanel([
            AssociationPanel('groups'),
        ], "Groups"),
    ]

    search_fields = [
        SearchField('family_name'),
        SearchField('given_names_and_initials')
    ]

    def __str__(self):
        return self.full_name


def protect(string):
    result = []

    for c in string:
        result.append(c)
        result.append("\u200B")

    result = "".join(result[:-1])
    return result


@register_snippet
class Group(Indexed, ClusterableModel):
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ['name']

        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='unique_%(app_label)s_%(class)s.identifier')
        ]

    @property
    def members_as_content(self):
        return [assignment.member for assignment in self.members.all()]

    identifier = django_models.CharField(max_length=128, default='', validators=[identifier_validator])
    active = django_models.BooleanField(verbose_name=_('active'), default=True, editable=True)
    name = CharField("Name", default="", max_length=192)

    short_description = RichTextField("Short Description", default="", editor=DEFAULT_RICH_TEXT_EDITOR,
                                      blank=True, null=True)

    panels = [

        MultiFieldPanel([

            FieldRowPanel([
                FieldPanel('name'),
                FieldPanel('identifier')
            ]),

            FieldPanel("short_description")

        ], "Description"),

        MultiFieldPanel([

            InlinePanel("members")

        ], "Members"),

    ]

    def __str__(self):
        return self.name


class GroupAssignment(Orderable):
    # noinspection SpellCheckingInspection
    """
    Meta must inherit from Orderable.Meta, otherwise the order of elements will not be saved in the admin interface!
    https://groups.google.com/forum/#!topic/wagtail/Ktk4RlnjWFM
    """

    class Meta(Orderable.Meta):
        verbose_name = 'Group Assignment'
        verbose_name_plural = 'Group Assignments'
        unique_together = (('group', 'member'),)

    active = django_models.BooleanField(verbose_name=_('active'), default=True, editable=True)

    group = ParentalKey(Group, related_name="members", on_delete=django_models.CASCADE, blank=False)
    member = ForeignKey(GroupMember, related_name="groups", on_delete=django_models.CASCADE, blank=False)

    short_description = RichTextField("Short Description", default="", editor=DEFAULT_RICH_TEXT_EDITOR,
                                      blank=True, null=True)

    visual = BlockModelField(MediaItemChooserBlock(
        max_num_choices=1,
        label="Visual",
        required=False),
        MediaItemChooserBlockValue, blank=True, null=True)

    link = BlockModelField(RichLinkBlock(label="Link"), RichLinkBlockValue, blank=True, null=True)

    panels = [
        FieldPanel('member'),
        FieldPanel('short_description'),
        FieldPanel('visual')
    ]

    @property
    def person(self):

        # noinspection PyUnresolvedReferences
        if self.member and isinstance(self.member.specific, Person):
            # noinspection PyUnresolvedReferences
            return self.member.specific
        return None

    @property
    def organisation(self):

        # noinspection PyUnresolvedReferences
        if self.member and isinstance(self.member.specific, Organisation):
            # noinspection PyUnresolvedReferences
            return self.member.specific
        return None
