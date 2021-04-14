"""LEHT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('checkout/', include('checkout.urls')),
    path('browser/', include('browser.urls')),
    path('navbar/', include('navbar.urls')),
    path('haldus/', include('haldus.urls')),
    path('favicon.ico',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'),
        ),
        name="favicon"
    ),
    url(r'^sitemaps.xml$',
        RedirectView.as_view( # the redirecting function
            url=staticfiles_storage.url('sitemaps.xml'), # converts the static directory + our favicon into a URL
            # in my case, the result would be http://www.tumblingprogrammer.com/static/img/favicon.ico
        ),
        name="favicon" # name of our view
    ),
    url(r'^sitemap.xml$',
        RedirectView.as_view( # the redirecting function
            url=staticfiles_storage.url('sitemaps.xml'), # converts the static directory + our favicon into a URL
            # in my case, the result would be http://www.tumblingprogrammer.com/static/img/favicon.ico
        ),
        name="favicon" # name of our view
    ),
    url(r'^robots.txt$',
        RedirectView.as_view( # the redirecting function
            url=staticfiles_storage.url('robots.txt'), # converts the static directory + our favicon into a URL
            # in my case, the result would be http://www.tumblingprogrammer.com/static/img/favicon.ico
        ),
        name="favicon" # name of our view
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

