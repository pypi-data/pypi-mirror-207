from django.urls import path

from .apps import get_app_label
from .content_admin import synopsis_admin

app_name = get_app_label()

urlpatterns = synopsis_admin.create_admin_urls() + [
]
