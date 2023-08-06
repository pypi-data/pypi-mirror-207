# -*- coding: utf-8 -*-

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

import wagtail.admin.rich_text.editors.draftail.features as builtin_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler, \
    InlineEntityElementHandler, BlockElementHandler

from draftjs_exporter.dom import DOM

from .apps import get_app_label

__all__ = ['register_style_feature', 'register_inline_entity_feature', 'register_embed_feature', 'register_block_feature']

APP_LABEL = get_app_label()

def register_style_feature(feature_name, feature_type, feature_tag, label, description, style, features):

    """
    Registering the `feature_name` feature, which uses the `feature_type` Draft.js inline style,
    and is stored as HTML with a `feature_tag` tag.
    """

    # 2. Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': feature_type,
        'label': label,
        'description': description,
        'style': style
    }

    # 3. Call register_editor_plugin to register the configuration for Draftail.
    features.register_editor_plugin(
        'draftail', feature_name, builtin_features.InlineStyleFeature(control)
    )

    # 4.configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {feature_tag: InlineStyleElementHandler(feature_type)},
        'to_database_format': {'style_map': {feature_type: feature_tag}},
    }

    # 5. Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)


def register_inline_entity_feature(feature_name, feature_type, feature_tag, label, description, features, css_classes=None, js_media_paths=None, css_media_paths=None):

    """
    Registering the `feature_name` feature, which uses the `feature_type` Draft.js inline style,
    and is stored as HTML with a `feature_tag` tag.
    """

    # 2. Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': feature_type,
        'label': label,
        'description': description,
        'cssClasses': css_classes if css_classes is not None else ''
    }

    entity_options = dict()
    entity_options['js'] = [tagged_static(APP_LABEL + '/js/draftail_helpers.js')]

    if js_media_paths:
        entity_options['js'] += [tagged_static(path) for path in js_media_paths]

    entity_options['css'] = {'all': [tagged_static(APP_LABEL + '/css/draftail_helpers.css')]}

    if css_media_paths:
        entity_options['css']['all']  += [tagged_static(path) for path in css_media_paths]

    # noinspection SpellCheckingInspection
    features.register_editor_plugin(

        'draftail', feature_name, builtin_features.EntityFeature(
            control,
            **entity_options
        )
    )

    class ElementHandler(InlineEntityElementHandler):
        mutability = 'MUTABLE'

        def get_attribute_data(self, attrs):
            return {
                'className': attrs.get('class', '')
            }

    def entity_data_to_db(props):

        attrs = {
            'class': props.get('className', '')
        }

        return DOM.create_element(feature_tag, attrs, props['children'])

    # 4.configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {feature_tag: ElementHandler(feature_type)},
        'to_database_format': {'entity_decorators': {feature_type: entity_data_to_db}},
    }

    # 5. Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)


def register_embed_feature(feature_name, feature_type, label, description,
                           embed_handler, entity_decorator, database_converter,
                           features,
                           key_binding=None, js_media_paths=None, css_media_paths=None):

    features.register_embed_type(embed_handler)

    control = {
        'type': feature_type,
        'label': label,
        'description': description
    }

    if key_binding is not None:
        control['key_binding'] = key_binding

    entity_options = dict()
    entity_options['js'] = [tagged_static(APP_LABEL + '/js/draftail_helpers.js')]

    if js_media_paths:
        entity_options['js'] += [tagged_static(path) for path in js_media_paths]

    entity_options['css'] = {'all': [tagged_static(APP_LABEL + '/css/draftail_helpers.css')]}

    if css_media_paths:
        entity_options['css']['all'] += [tagged_static(path) for path in css_media_paths]

    # noinspection SpellCheckingInspection
    features.register_editor_plugin(

        'draftail', feature_name, builtin_features.EntityFeature(
            control,
            **entity_options
        )
    )

    selector = 'embed[embedtype="{}"]'.format(feature_name)

    conversion_specifier = {
        'from_database_format': {selector: database_converter},
        'to_database_format': {'entity_decorators': {feature_type: entity_decorator}},
    }

    features.register_converter_rule('contentstate', feature_name, conversion_specifier)


def register_block_feature(feature_name, feature_type, feature_tag, label, description, features,
                           js_media_paths=None, css_media_paths=None):

    """
    Registering the `feature_name` feature, which uses the `feature_type` Draft.js inline style,
    and is stored as HTML with a `feature_tag` tag.
    """

    # 2. Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': feature_type,
        'label': label,
        'description': description,
        'element': feature_tag,
    }

    entity_options = dict()
    entity_options['js'] = [tagged_static(APP_LABEL + '/js/draftail_helpers.js')]

    if js_media_paths:
        entity_options['js'] += [tagged_static(path) for path in js_media_paths]

    entity_options['css'] = {'all': [tagged_static(APP_LABEL + '/css/draftail_helpers.css')]}

    if css_media_paths:
        entity_options['css']['all'] += [tagged_static(path) for path in css_media_paths]

    # 3. Call register_editor_plugin to register the configuration for Draftail.
    features.register_editor_plugin(
        'draftail', feature_name, builtin_features.BlockFeature(control, **entity_options)
    )

    # 4.configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {feature_tag: BlockElementHandler(feature_type)},
        'to_database_format': {'block_map': {feature_type: feature_tag}},
    }

    # 5. Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)

