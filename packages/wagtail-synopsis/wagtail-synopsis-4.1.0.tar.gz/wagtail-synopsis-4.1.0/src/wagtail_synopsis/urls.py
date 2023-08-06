from django.urls import re_path

from .content_admin import synopsis_admin
from .apps import get_app_label

app_name = get_app_label()

urlpatterns = synopsis_admin.create_urls() + [
]
