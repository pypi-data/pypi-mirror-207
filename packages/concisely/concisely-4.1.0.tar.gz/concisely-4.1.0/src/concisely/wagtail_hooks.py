
from wagtail.core import hooks

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

from .semantic_features import feature_registrations as semantic_features

features_to_register = semantic_features

for register_feature in features_to_register:
    hooks.register('register_rich_text_features', fn=register_feature)


@hooks.register('register_rich_text_area_media_settings')
def text_area_media_settings():
    return {
        'js': [
                 tagged_static('wagtailadmin/js/draftail_control_feature.js'),
                 tagged_static('wagtailadmin/js/draftail_plugin_support.js'),
                 tagged_static('draftail_helpers/js/draftail_helpers.js'),
                 tagged_static('concisely/js/concisely.js')
             ],
        'css': {
            'all': [tagged_static('draftail_helpers/css/draftail_helpers.css'),
                    tagged_static('concisely/css/concisely.css')]
        }
    }
