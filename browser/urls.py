from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.browser),
    path("import/", views.browser_import),
    path("categories/", views.categories),
    path("reset/", views.reset_filters),
    re_path(r'^product/(?P<code>.*)$', views.product),
    re_path(r'^categories/(?P<main_cat>.*)/(?P<cat>.*)$', views.categories_filter)
]