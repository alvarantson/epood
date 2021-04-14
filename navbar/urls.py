from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^change_lang/(?P<lang>.*)$', views.change_lang)
]