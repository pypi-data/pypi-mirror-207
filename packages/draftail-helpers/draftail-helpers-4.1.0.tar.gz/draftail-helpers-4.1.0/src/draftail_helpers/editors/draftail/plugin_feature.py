# -*- coding: utf-8 -*-

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static
import wagtail.admin.rich_text.editors.draftail.features as builtin_features

from .control_feature import ControlFeature

from draftail_helpers.apps import get_app_label

APP_LABEL = get_app_label()


class PluginFeature(builtin_features.ListFeature):
    """A feature which is listed in the controls list of the options"""
    option_name = 'plugins'

    # noinspection SpellCheckingInspection
    js = tagged_static(APP_LABEL + '/js/draftail_plugin_support.js')

    def __init__(self, data, **kwargs):

        js = kwargs.setdefault("js", [PluginFeature.js])

        if PluginFeature.js not in js:
            js.insert(0, PluginFeature.js)

        if "control" in data:

            data = dict(data)
            self.control = data.pop("control", None)

            if ControlFeature.js not in js:
                js.insert(0, ControlFeature.js)
        else:
            self.control = None

        super().__init__(data, **kwargs)

    def construct_options(self, options):

        super().construct_options(options)

        if self.control:

            if "controls" not in options:
                options["controls"] = []

            options["controls"].append(self.control)
