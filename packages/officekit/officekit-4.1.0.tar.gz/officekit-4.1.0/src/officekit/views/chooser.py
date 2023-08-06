from django.utils.functional import cached_property

from wagtail.coreutils import resolve_model_string
from wagtail.admin.views.generic.chooser import ChooseViewMixin, CreationFormMixin, BaseChooseView, \
    ChooseResultsViewMixin, ChosenView

from ..apps import get_app_label

APP_LABEL = get_app_label()


class GroupMemberBaseChooseView(BaseChooseView): # noqa

    model = APP_LABEL + ".groupmember" # noqa
    specific_models = []

    @cached_property
    def specific_model_classes(self):
        if self.specific_models:
            return [resolve_model_string(specific_model) for specific_model in self.specific_models]

        return []

    @cached_property
    def specific_model_content_type_ids(self):
        return [specific_model_class.content_type_id for specific_model_class in self.specific_model_classes]

    def get_object_list(self):

        if self.specific_model_content_type_ids:
            return self.model_class.objects.all().filter(content_type_id__in=self.specific_model_content_type_ids).specific()
        else:
            return self.model_class.objects.all().specific()


class GroupMemberChooseView(ChooseViewMixin, CreationFormMixin, GroupMemberBaseChooseView):
    pass


class GroupMemberChooseResultsView(ChooseResultsViewMixin, CreationFormMixin, GroupMemberBaseChooseView):
    pass


class GroupMemberChosenView(ChosenView):

    def get_object(self, pk):
        result = self.model_class.objects.get(pk=pk)
        result = result.specific if result else result
        return result
