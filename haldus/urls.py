from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.haldus),
    path("discount/", views.discount),
    path("salesstats/", views.salesstats),
]