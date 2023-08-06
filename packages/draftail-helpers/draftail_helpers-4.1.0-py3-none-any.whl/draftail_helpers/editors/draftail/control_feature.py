# -*- coding: utf-8 -*-

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static
import wagtail.admin.rich_text.editors.draftail.features as builtin_features

from draftail_helpers.apps import get_app_label

APP_LABEL = get_app_label()


class ControlFeature(builtin_features.ListFeature):
    """A feature which is listed in the controls list of the options"""
    option_name = 'controls'

    # noinspection SpellCheckingInspection
    js = tagged_static(APP_LABEL + '/js/draftail_control_feature.js')

    def __init__(self, data, **kwargs):

        js = kwargs.setdefault("js", [ControlFeature.js])

        if ControlFeature.js not in js:
            js.insert(0, ControlFeature.js)

        super().__init__(data, **kwargs)
