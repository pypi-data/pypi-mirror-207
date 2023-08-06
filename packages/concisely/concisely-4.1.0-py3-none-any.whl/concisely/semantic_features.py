# -*- coding: utf-8 -*-

from wagtail.admin.rich_text.converters.html_to_contentstate import AtomicBlockEntityElementHandler, Entity
from wagtail.rich_text import EmbedHandler
from draftjs_exporter.dom import DOM

__all__ = ['CITATION_FEATURE_NAME', 'register_citation_feature',
           'QUOTATION_FEATURE_NAME', 'register_quotation_feature',
           'EMPHASIS_FEATURE_NAME', 'register_emphasis_feature',
           'ATTENTION_FEATURE_NAME', 'register_attention_feature',
           'IMPORTANCE_FEATURE_NAME', 'register_importance_feature',
           'DEFINITION_FEATURE_NAME', 'register_definition_feature',
           'ALTERNATION_FEATURE_NAME', 'register_alternation_feature',
           'SMALL_FEATURE_NAME', 'register_small_feature',
           'ABBREVIATION_FEATURE_NAME', 'register_abbreviation_feature',
           'USER_INPUT_FEATURE_NAME', 'register_user_input_feature',
           'SYSTEM_OUTPUT_FEATURE_NAME', 'register_system_output_feature',
           'CODE_FEATURE_NAME', 'register_code_feature',
           'VARIABLE_FEATURE_NAME', 'register_variable_feature',
           'SUBSCRIPT_FEATURE_NAME', 'register_subscript_feature',
           'SUPERSCRIPT_FEATURE_NAME', 'register_superscript_feature',
           'INSERTION_FEATURE_NAME', 'register_insertion_feature',
           'DELETION_FEATURE_NAME', 'register_deletion_feature',
           'PREFORMATTED_FEATURE_NAME', 'register_preformatted_feature',
           'BLOCKQUOTE_FEATURE_NAME', 'register_blockquote_feature',
           'HEADING_FEATURE_NAME', 'register_heading_feature',
           'feature_names', 'feature_registrations'
           ]


CITATION_FEATURE_NAME = 'concisely.citation'
CITATION_ENTITY_TYPE = 'concisely.CITATION'
CITATION_FEATURE_TAG = 'cite'


def register_citation_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    """
    register_inline_entity_feature(CITATION_FEATURE_NAME,
                               CITATION_ENTITY_TYPE,
                               CITATION_FEATURE_TAG,
                               'Cite',
                               'Reference to a creative work, such as a book, a research paper, a web page, etc.',
                               features,
                               'concisely-cite'
                               )
    """

    register_style_feature(CITATION_FEATURE_NAME,
                           CITATION_ENTITY_TYPE,
                           CITATION_FEATURE_TAG,
                           'Cite',
                           'Reference to a creative work, such as a book, a research paper, a web page, etc.',
                           {'textDecoration': 'underline overline', 'color': 'purple'},
                           features)


QUOTATION_FEATURE_NAME = 'concisely.quotation'
QUOTATION_ENTITY_TYPE = 'concisely.QUOTATION'
QUOTATION_FEATURE_TAG = 'q'


def register_quotation_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(QUOTATION_FEATURE_NAME,
                           QUOTATION_ENTITY_TYPE,
                           QUOTATION_FEATURE_TAG,
                           'Q',
                           'Verbatim inline quote from a cited source',
                           {'textDecoration': 'underline overline', 'color': 'purple'},
                           features)


EMPHASIS_FEATURE_NAME = 'concisely.emphasis'
EMPHASIS_ENTITY_TYPE = 'concisely.EMPHASIS'
EMPHASIS_FEATURE_TAG = 'em'


def register_emphasis_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(EMPHASIS_FEATURE_NAME,
                           EMPHASIS_ENTITY_TYPE,
                           EMPHASIS_FEATURE_TAG,
                           'Em',
                           'Indicate (spoken) stress',
                           {'fontStyle': 'italic'},
                           features)


ATTENTION_FEATURE_NAME = 'concisely.attention'
ATTENTION_ENTITY_TYPE = 'concisely.ATTENTION'
ATTENTION_FEATURE_TAG = 'b'


def register_attention_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(ATTENTION_FEATURE_NAME,
                           ATTENTION_ENTITY_TYPE,
                           ATTENTION_FEATURE_TAG,
                           'Att',
                           'Draw visual attention, but without implied importance.',
                           {'fontWeight': 600},
                           features)


IMPORTANCE_FEATURE_NAME = 'concisely.importance'
IMPORTANCE_ENTITY_TYPE = 'concisely.IMPORTANCE'
IMPORTANCE_FEATURE_TAG = 'strong'


def register_importance_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(IMPORTANCE_FEATURE_NAME,
                           IMPORTANCE_ENTITY_TYPE,
                           IMPORTANCE_FEATURE_TAG,
                           '!',
                           'Mark as important, serious or urgent',
                           {'textDecoration': 'underline'},
                           features)


DEFINITION_FEATURE_NAME = 'concisely.definition'
DEFINITION_ENTITY_TYPE = 'concisely.DEFINITION'
DEFINITION_FEATURE_TAG = 'dfn'


def register_definition_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(DEFINITION_FEATURE_NAME,
                           DEFINITION_ENTITY_TYPE,
                           DEFINITION_FEATURE_TAG,
                           'Def',
                           'Highlight the term being defined.',
                           {'textDecoration': 'overline', 'color': 'green'},
                           features)


ALTERNATION_FEATURE_NAME = 'concisely.alternation'
ALTERNATION_ENTITY_TYPE = 'concisely.ALTERNATION'
ALTERNATION_FEATURE_TAG = 'i'


def register_alternation_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(ALTERNATION_FEATURE_NAME,
                           ALTERNATION_ENTITY_TYPE,
                           ALTERNATION_FEATURE_TAG,
                           'Alt',
                           'Indicate different quality of text, such as a taxonomic designation, a technical term, or an idiomatic phrase from another language',
                           {'fontFamily': 'serif', 'fontStyle': 'oblique', 'fontWeight': 300},
                           features)


SMALL_FEATURE_NAME = 'concisely.small'
SMALL_ENTITY_TYPE = 'concisely.SMALL'
SMALL_FEATURE_TAG = 'small'


def register_small_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(SMALL_FEATURE_NAME,
                           SMALL_ENTITY_TYPE,
                           SMALL_FEATURE_TAG,
                           'Small',
                           'Represents side-comments and small print, like copyright and legal text, ' +
                           'independent of its styled presentation.',
                           {'fontSize': 'smaller'},
                           features)


ABBREVIATION_FEATURE_NAME = 'concisely.abbreviation'
ABBREVIATION_ENTITY_TYPE = 'concisely.ABBREVIATION'
ABBREVIATION_FEATURE_TAG = 'abbr'


def register_abbreviation_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(ABBREVIATION_FEATURE_NAME,
                           ABBREVIATION_ENTITY_TYPE,
                           ABBREVIATION_FEATURE_TAG,
                           'Abbr',
                           'Represents an abbreviation or acronym.',
                           {'textDecoration': 'line-through', 'color': 'green'},
                           features)


USER_INPUT_FEATURE_NAME = 'concisely.input'
USER_INPUT_ENTITY_TYPE = 'concisely.INPUT'
USER_INPUT_FEATURE_TAG = 'kbd'


def register_user_input_feature(features):
    #  'boxShadow': '0 1px 1px rgba(0, 0, 0, .2), 0 2px 0 0 rgba(255, 255, 255, .7) inset',
    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(USER_INPUT_FEATURE_NAME,
                           USER_INPUT_ENTITY_TYPE,
                           USER_INPUT_FEATURE_TAG,
                           'Input',
                           'Represents user input such as key presses or voice commands',
                           {'whiteSpace': 'nowrap', 'fontFamily': 'monospace', 'backgroundColor': 'hsl(0, 0%, 96%)',
                            'borderRadius': '3px',
                            'border': '1px solid hsl(0, 0%, 80%)',
                            'padding': '3px'
                            },
                           features)


SYSTEM_OUTPUT_FEATURE_NAME = 'concisely.output'
SYSTEM_OUTPUT_ENTITY_TYPE = 'concisely.OUTPUT'
SYSTEM_OUTPUT_FEATURE_TAG = 'samp'


def register_system_output_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(SYSTEM_OUTPUT_FEATURE_NAME,
                           SYSTEM_OUTPUT_ENTITY_TYPE,
                           SYSTEM_OUTPUT_FEATURE_TAG,
                           'Output',
                           'Represents output from a system.',
                           {'fontFamily': 'monospace', 'color': 'darkgreen', 'fontWeight': 500},
                           features)


CODE_FEATURE_NAME = 'concisely.code'
CODE_ENTITY_TYPE = 'concisely.CODE'
CODE_FEATURE_TAG = 'code'


def register_code_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(CODE_FEATURE_NAME,
                           CODE_ENTITY_TYPE,
                           CODE_FEATURE_TAG,
                           'Code',
                           'A snippet of computer code.',
                           {'fontFamily': 'monospace'},
                           features)


VARIABLE_FEATURE_NAME = 'concisely.variable'
VARIABLE_ENTITY_TYPE = 'concisely.VARIABLE'
VARIABLE_FEATURE_TAG = 'var'


def register_variable_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(VARIABLE_FEATURE_NAME,
                           VARIABLE_ENTITY_TYPE,
                           VARIABLE_FEATURE_TAG,
                           'Var',
                           'Indicates a variable.',
                           {'fontFamily': 'monospace'},
                           features)


SUBSCRIPT_FEATURE_NAME = 'concisely.subscript'
SUBSCRIPT_ENTITY_TYPE = 'concisely.SUBSCRIPT'
SUBSCRIPT_FEATURE_TAG = 'sub'


def register_subscript_feature(features):
    # {'fontSize': 'small', 'position': 'relative', 'top': '0.4em'},
    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(SUBSCRIPT_FEATURE_NAME,
                           SUBSCRIPT_ENTITY_TYPE,
                           SUBSCRIPT_FEATURE_TAG,
                           'Sub',
                           'Subscript',
                           {'fontSize': 'small', 'vertical-align': 'sub'},
                           features)


SUPERSCRIPT_FEATURE_NAME = 'concisely.superscript'
SUPERSCRIPT_ENTITY_TYPE = 'concisely.SUPERSCRIPT'
SUPERSCRIPT_FEATURE_TAG = 'sup'


def register_superscript_feature(features):

    from draftail_helpers.feature_registry import register_style_feature

    # {'fontSize': 'small', 'position': 'relative', 'bottom': '0.6em'},

    register_style_feature(SUPERSCRIPT_FEATURE_NAME,
                           SUPERSCRIPT_ENTITY_TYPE,
                           SUPERSCRIPT_FEATURE_TAG,
                           'Sup',
                           'Superscript',
                           {'fontSize': 'small', 'vertical-align': 'super'},
                           features)


DELETION_FEATURE_NAME = 'concisely.deletion'
DELETION_ENTITY_TYPE = 'concisely.DELETION'
DELETION_FEATURE_TAG = 'del'


def register_deletion_feature(features):
    from draftail_helpers.feature_registry import register_style_feature

    register_style_feature(DELETION_FEATURE_NAME,
                           DELETION_ENTITY_TYPE,
                           DELETION_FEATURE_TAG,
                           'Deleted',
                           'Indicate a deletion edit.',
                           {'textDecoration': 'line-through', 'textDecorationColor': 'red', 'color': 'hsl(0, 0%, 30%)',
                            'textDecorationThickness': '2px'},
                           features)


INSERTION_FEATURE_NAME = 'concisely.insertion'
INSERTION_ENTITY_TYPE = 'concisely.INSERTION'
INSERTION_FEATURE_TAG = 'ins'


def register_insertion_feature(features):
    from draftail_helpers.feature_registry import register_style_feature
    # hsl(204, 50%, 50%)
    register_style_feature(INSERTION_FEATURE_NAME,
                           INSERTION_ENTITY_TYPE,
                           INSERTION_FEATURE_TAG,
                           'Inserted',
                           'Indicate an insertion edit.',
                           {'borderLeft': 'solid 2px rgb(68, 191, 64)', 'borderBottom': 'solid 2px rgb(68, 191, 64)',
                            'borderRight': 'solid 2px rgb(68, 191, 64)',
                            'borderBottomLeftRadius': '3px', 'borderBottomRightRadius': '3px',
                            'paddingLeft': '2px', 'paddingRight': '2px'},
                           features)


BLOCKQUOTE_FEATURE_NAME = 'concisely.blockquote'
BLOCKQUOTE_ENTITY_TYPE = 'concisely.BLOCKQUOTE'
BLOCKQUOTE_FEATURE_TAG = 'blockquote'


def register_blockquote_feature(features):
    from draftail_helpers.feature_registry import register_block_feature

    register_block_feature(BLOCKQUOTE_FEATURE_NAME,
                           BLOCKQUOTE_ENTITY_TYPE,
                           BLOCKQUOTE_FEATURE_TAG,
                           'Block Quote',
                           'Represent a section quoted from another source.',
                           features)


PREFORMATTED_FEATURE_NAME = 'concisely.preformatted'
PREFORMATTED_ENTITY_TYPE = 'concisely.PREFORMATTED'
PREFORMATTED_FEATURE_TAG = 'pre'


def register_preformatted_feature(features):
    from draftail_helpers.feature_registry import register_block_feature

    register_block_feature(PREFORMATTED_FEATURE_NAME,
                           PREFORMATTED_ENTITY_TYPE,
                           PREFORMATTED_FEATURE_TAG,
                           'Pre',
                           'Keep formatting such as line breaks and whitespace.',
                           features)


HEADING_FEATURE_NAME = 'concisely.heading'
HEADING_ENTITY_TYPE = 'concisely.HEADING'

EDITOR_SETTINGS_PROPERTY = "editor_settings"
HEADING_CONTENT_PROPERTY = "content"


def heading_entity_data_to_db(props):

    attrs = {
        'data-' + EDITOR_SETTINGS_PROPERTY: props.get(EDITOR_SETTINGS_PROPERTY, ""),
    }

    attrs.update({
        'embedtype': HEADING_FEATURE_NAME,
        'data-' + HEADING_CONTENT_PROPERTY: props[HEADING_CONTENT_PROPERTY]
    })

    return DOM.create_element("embed", attrs, props['children'])


def heading_db_to_editor_entity_data(attrs):

    props = {
        EDITOR_SETTINGS_PROPERTY: attrs.get('data-' + EDITOR_SETTINGS_PROPERTY, "")
    }

    props.update({
        HEADING_CONTENT_PROPERTY: attrs['data-' + HEADING_CONTENT_PROPERTY]
    })

    return props


def heading_db_to_frontend_html(attrs):

    content = attrs.get('data-' + HEADING_CONTENT_PROPERTY)
    result = '<h6>{}</h6>'.format(content)
    return result


class HeadingHandler(AtomicBlockEntityElementHandler):

    # noinspection PyMethodMayBeStatic
    # noinspection SpellCheckingInspection
    def create_entity(self, name, attrs, state, contentstate):
        return Entity(HEADING_ENTITY_TYPE, "MUTABLE", heading_db_to_editor_entity_data(attrs))


class HeadingEmbedHandler(EmbedHandler):

    identifier = HEADING_FEATURE_NAME

    @staticmethod
    def get_model():
        raise NotImplementedError

    @staticmethod
    def expand_db_attributes(attrs):
        return heading_db_to_frontend_html(attrs)


def register_heading_feature(features):
    from draftail_helpers.feature_registry import register_embed_feature

    register_embed_feature(HEADING_FEATURE_NAME,
                           HEADING_ENTITY_TYPE,
                           'H',
                           'Heading',
                           HeadingEmbedHandler(),  # embed_handler
                           lambda props: heading_entity_data_to_db(props),  # entity_decorator
                           HeadingHandler(),  # database_converter
                           features)


feature_registrations = [register_citation_feature, register_quotation_feature, register_emphasis_feature,
                         register_attention_feature, register_importance_feature, register_definition_feature,
                         register_alternation_feature, register_small_feature, register_abbreviation_feature,
                         register_user_input_feature, register_system_output_feature,
                         register_code_feature, register_variable_feature,
                         register_subscript_feature, register_superscript_feature,
                         register_insertion_feature, register_deletion_feature,
                         register_blockquote_feature, register_preformatted_feature,
                         register_heading_feature
                         ]

feature_names = [CITATION_FEATURE_NAME, QUOTATION_FEATURE_NAME, EMPHASIS_FEATURE_NAME,
                 ATTENTION_FEATURE_NAME, IMPORTANCE_FEATURE_NAME, DEFINITION_FEATURE_NAME,
                 ALTERNATION_FEATURE_NAME, SMALL_FEATURE_NAME, ABBREVIATION_FEATURE_NAME,
                 USER_INPUT_FEATURE_NAME, SYSTEM_OUTPUT_FEATURE_NAME,
                 CODE_FEATURE_NAME, VARIABLE_FEATURE_NAME,
                 SUBSCRIPT_FEATURE_NAME, SUPERSCRIPT_FEATURE_NAME,
                 INSERTION_FEATURE_NAME, DELETION_FEATURE_NAME,
                 BLOCKQUOTE_FEATURE_NAME, PREFORMATTED_FEATURE_NAME,
                 HEADING_FEATURE_NAME
                 ]

