
from wagtail.permission_policies import BlanketPermissionPolicy

from wagtail_content_admin.content_admin import ContentAdmin
from wagtail_richer_text.templatetags.wagtail_richer_text_tags import richertext

from .apps import get_app_label

__all__ = ['synopsis_admin', 'SynopsisAdmin']

APP_LABEL = get_app_label()


class SynopsisAdmin(ContentAdmin):

    browser_order_by = ['-created_at']
    url_namespace = APP_LABEL
    permission_policy = BlanketPermissionPolicy(APP_LABEL + ".synopsis")

    def __init__(self):
        super(SynopsisAdmin, self).__init__()

    def render_choice_inner(self, instance, **kwargs):
        result = richertext(instance.summary)
        return result

    def render_preview_inner(self, instance, **kwargs):
        result = richertext(instance.summary)


        """
          <h3 class="abstract-heading">
  {% if layout.template_values.show_rubrics %}{% if synopsis.rubric_url %}<a class="abstract-rubric" href="{{ synopsis.rubric_url }}">{{ synopsis.rubric }}</a>{% else %}{{ synopsis.rubric }}{% endif %}{% endif %}
  {% if synopsis.has_destination_url %}<a href="{% synopsis_destination_url synopsis request=request %}">{{ synopsis.heading }}</a>{% else %}{{ synopsis.heading }}{% endif %}</h3>
  {% if layout.template_values.show_publishing_date %}{% if synopsis.created_at or synopsis.updated_at %}
  <p class="abstract-dateline"><span class="abstract-publishing-date">{% if synopsis.updated_at %}{{ synopsis.updated_at }}{% else %}{{ synopsis.created_at }}{% endif %}</span></p>
  {% endif %}{% endif %}
          <div class="abstract-summary">{{ synopsis.summary|richertext }}</div>
        """

        return result


synopsis_admin = SynopsisAdmin()
