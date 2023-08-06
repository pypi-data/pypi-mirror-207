from wagtail import hooks

from django.template.loader import render_to_string

from .templatetags.draftail_maths_tags import draftail_maths_support_tag

from .maths_features import feature_registrations as maths_features
from .apps import get_app_label


APP_LABEL = get_app_label()

features_to_register = maths_features


@hooks.register('insert_global_admin_js')
def insert_vendor_js():
    context = draftail_maths_support_tag(
                container_element='head',
                mathjax_version='2.7.6',
                is_admin_page=True)

    return render_to_string(template_name=APP_LABEL + "/tags/support.html", context=context)


for register_feature in features_to_register:
    hooks.register('register_rich_text_features', fn=register_feature)