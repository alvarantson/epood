from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.checkout),
    path("empty/", views.empty),
    re_path(r'^add/(?P<code>.*)/(?P<qty>.*)$', views.add),
    re_path(r'^qty/(?P<code>.*)/(?P<qty>.*)$', views.qty),
    path("charge/", views.charge, name='charge'),
    re_path(r'^remove/(?P<code>.*)$', views.remove)
]