# -*- coding: utf-8 -*-

from django.conf import settings

from wagtail.admin.rich_text.converters.html_to_contentstate import AtomicBlockEntityElementHandler, \
                                                                    InlineEntityElementHandler, Entity, KEEP_WHITESPACE
from wagtail.rich_text import EmbedHandler

from draftjs_exporter.dom import DOM

from .maths_feature_names import *

import re

"""

MATH entity:

    syntax_specifier: ['TeX', 'MathML', 'AsciiMath']
    content_as_specified: 'some string'
    content_as_math_ml: '<math>...</math>'

"""

MATH_ML_SYNTAX = 'MathML'
TEX_SYNTAX = 'TeX'
ASCII_MATH_SYNTAX = 'AsciiMath'

SYNTAX_SPECIFIER_PROPERTY = "syntax_specifier"
CONTENT_AS_SPECIFIED_PROPERTY = "content_as_specified"
CONTENT_AS_MATH_ML_PROPERTY = "content_as_math_ml"
ANCHOR_IDENTIFIER_PROPERTY = "anchor_identifier"
ANCHOR_LEVEL_PROPERTY = "anchor_level"

EDITOR_SETTINGS_PROPERTY = "editor_settings"

BLOCK_MATHS_ANCHOR_CATEGORY = "equation"


def editor_entity_data_to_html_attributes(props):

    attrs = {
        'data-' + EDITOR_SETTINGS_PROPERTY: props.get(EDITOR_SETTINGS_PROPERTY, ""),
    }

    return attrs


def html_attributes_to_editor_entity_data(attrs):

    props = {
        EDITOR_SETTINGS_PROPERTY: attrs.get('data-' + EDITOR_SETTINGS_PROPERTY, "")
    }

    return props


def math_editor_entity_data_to_db(props, is_inline_entity):

    attrs = editor_entity_data_to_html_attributes(props)

    attrs.update({
        'embedtype': INLINE_MATHS_FEATURE_NAME if is_inline_entity else BLOCK_MATHS_FEATURE_NAME,
        'data-' + SYNTAX_SPECIFIER_PROPERTY: props[SYNTAX_SPECIFIER_PROPERTY],
        'data-' + CONTENT_AS_SPECIFIED_PROPERTY: props[CONTENT_AS_SPECIFIED_PROPERTY],
        'data-' + CONTENT_AS_MATH_ML_PROPERTY: props[CONTENT_AS_MATH_ML_PROPERTY],
        'data-' + ANCHOR_IDENTIFIER_PROPERTY: props[ANCHOR_IDENTIFIER_PROPERTY],
        'data-' + ANCHOR_LEVEL_PROPERTY: props[ANCHOR_LEVEL_PROPERTY]
    })

    return DOM.create_element("embed", attrs, props['children'])


def math_db_to_editor_entity_data(attrs):

    props = html_attributes_to_editor_entity_data(attrs)

    props.update({
        SYNTAX_SPECIFIER_PROPERTY: attrs['data-' + SYNTAX_SPECIFIER_PROPERTY],
        CONTENT_AS_SPECIFIED_PROPERTY: attrs['data-' + CONTENT_AS_SPECIFIED_PROPERTY],
        CONTENT_AS_MATH_ML_PROPERTY: attrs['data-' + CONTENT_AS_MATH_ML_PROPERTY],
        ANCHOR_IDENTIFIER_PROPERTY: attrs['data-' + ANCHOR_IDENTIFIER_PROPERTY],
        ANCHOR_LEVEL_PROPERTY: attrs['data-' + ANCHOR_LEVEL_PROPERTY]
    })

    return props


WHITESPACE_RE = re.compile("(\\s+)$", re.UNICODE)


def math_db_to_frontend_html(attrs, is_inline_entity):

    extra_content = ""
    anchor_id = None
    anchor_label = ''
    anchor_identifier = attrs.get('data-' + ANCHOR_IDENTIFIER_PROPERTY, '')

    if is_inline_entity:
        specified_content = attrs['data-' + CONTENT_AS_SPECIFIED_PROPERTY]
        match = WHITESPACE_RE.search(specified_content)

        if match:
            extra_content = match.group(1)
    elif anchor_identifier:
        from tour_guide.anchors import current_anchor_registry_and_inventory

        try:
            anchor_level = int(attrs.get('data-' + ANCHOR_LEVEL_PROPERTY, 0))
        except ValueError:
            anchor_level = 0

        registry, inventory = current_anchor_registry_and_inventory()
        anchor_id = registry.define_anchor(inventory, BLOCK_MATHS_ANCHOR_CATEGORY, anchor_identifier, anchor_level)
        anchor_label = registry.label_anchor(inventory, BLOCK_MATHS_ANCHOR_CATEGORY, anchor_identifier, 'short_label')

    # MathJax v2: result = "<script type=\"{}\">".format("math/mml") + attrs['data-' + CONTENT_AS_MATH_ML_PROPERTY] + "</script>"
    result = attrs['data-' + CONTENT_AS_MATH_ML_PROPERTY]

    if anchor_id and result.startswith('<math '):

        result = '<div class="{}" id="{}"><div><span class="anchor-label">{}</span></div><math '.format(
                    settings.DRAFTAIL_MATHS_EQUATION_CLASSNAME, anchor_id, anchor_label) + result[6:] + '</div>'

    result += extra_content
    return result


class InlineMathsEmbedHandler(EmbedHandler):

    identifier = INLINE_MATHS_FEATURE_NAME

    @staticmethod
    def get_model():
        raise NotImplementedError

    @staticmethod
    def expand_db_attributes(attrs):
        return math_db_to_frontend_html(attrs, True)


class InlineMathHandler(InlineEntityElementHandler):

    mutability = "IMMUTABLE"

    def __init__(self):
        super().__init__(INLINE_MATHS_ENTITY_TYPE)
        self.placeholder_text = "[math]"

    def get_attribute_data(self, attrs):
        result = math_db_to_editor_entity_data(attrs)
        self.placeholder_text = result.get(CONTENT_AS_SPECIFIED_PROPERTY, self.placeholder_text)
        return result

    # noinspection SpellCheckingInspection
    def handle_endtag(self, name, state, contentstate):
        state.current_block.text += self.placeholder_text
        super().handle_endtag(name, state, contentstate)
        state.leading_whitespace = KEEP_WHITESPACE


def register_inline_maths_feature(features):
    from draftail_helpers.feature_registry import register_embed_feature

    register_embed_feature(INLINE_MATHS_FEATURE_NAME,
                           INLINE_MATHS_ENTITY_TYPE,
                           'Expression',
                           'Mathematical Expression',
                           InlineMathsEmbedHandler(),  # embed_handler
                           lambda props: math_editor_entity_data_to_db(props, True),  # entity_decorator
                           InlineMathHandler(),  # database_converter
                           features,
                           key_binding='$',
                           js_media_paths=['draftail_maths/js/draftail_maths.js'],
                           css_media_paths=['draftail_maths/css/draftail_maths.css'])


class BlockMathHandler(AtomicBlockEntityElementHandler):

    # noinspection PyMethodMayBeStatic
    # noinspection SpellCheckingInspection
    def create_entity(self, name, attrs, state, contentstate):
        return Entity(BLOCK_MATHS_ENTITY_TYPE, "IMMUTABLE", math_db_to_editor_entity_data(attrs))


class BlockMathsEmbedHandler(EmbedHandler):

    identifier = BLOCK_MATHS_FEATURE_NAME

    @staticmethod
    def get_model():
        raise NotImplementedError

    @staticmethod
    def expand_db_attributes(attrs):
        return math_db_to_frontend_html(attrs, False)


def register_block_maths_feature(features):
    from draftail_helpers.feature_registry import register_embed_feature

    register_embed_feature(BLOCK_MATHS_FEATURE_NAME,
                           BLOCK_MATHS_ENTITY_TYPE,
                           'Equation',
                           'Mathematical Equation',
                           BlockMathsEmbedHandler(),  # embed_handler
                           lambda props: math_editor_entity_data_to_db(props, False),  # entity_decorator
                           BlockMathHandler(),  # database_converter
                           features,
                           js_media_paths=['draftail_maths/js/draftail_maths.js'],
                           css_media_paths=['draftail_maths/css/draftail_maths.css'])


feature_registrations = [register_inline_maths_feature, register_block_maths_feature
                         ]

feature_names = [INLINE_MATHS_FEATURE_NAME, BLOCK_MATHS_FEATURE_NAME
                 ]
