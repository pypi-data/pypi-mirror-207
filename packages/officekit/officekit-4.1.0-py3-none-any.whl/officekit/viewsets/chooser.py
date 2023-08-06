
from wagtail.admin.viewsets.chooser import ChooserViewSet

from ..views.chooser import GroupMemberChooseView, GroupMemberChosenView, GroupMemberChooseResultsView
from ..widgets import BaseGroupMemberChooser
from ..apps import get_app_label

APP_LABEL = get_app_label()


def create_group_member_viewset(name, url_prefix, common_class_prefix, specific_models=None):

    if specific_models is None:
        specific_models = []

    def init_choose_view(self, *args, **kwargs):
        GroupMemberChooseView.__init__(self, *args, specific_models=specific_models, **kwargs) # noqa


    ChooseViewClass = type(common_class_prefix + "ChooseView", (GroupMemberChooseView,), {'__module__': __name__, '__init__': init_choose_view}) # noqa

    def init_choose_results_view(self, *args, **kwargs):
        GroupMemberChooseResultsView.__init__(self, *args, specific_models=specific_models, **kwargs) # noqa

    ChooseResultsViewClass = type(common_class_prefix + "ChooseResultsView", (GroupMemberChooseResultsView,), {'__module__': __name__, '__init__': init_choose_results_view}) # noqa

    def init_chosen_view(self, *args, **kwargs):
        GroupMemberChosenView.__init__(self, *args, specific_models=specific_models, **kwargs) # noqa

    ChosenViewClass = type(common_class_prefix + "ChosenView", (GroupMemberChosenView,), {'__module__': __name__, '__init__': init_chosen_view}) # noqa

    viewset = ChooserViewSet(name,
                             url_prefix=url_prefix + "/" + name,
                             model=APP_LABEL + ".GroupMember",
                             base_widget_class=BaseGroupMemberChooser,
                             choose_view_class=ChooseViewClass,
                             choose_results_view_class=ChooseResultsViewClass,
                             chosen_view_class=ChosenViewClass)
    return viewset
