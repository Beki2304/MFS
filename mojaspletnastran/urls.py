"""mojaspletnastran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   url("^kljuc$", "blog.views.vprasanje"),
  url("^kljuc/(?P<id>[0-9]+)/$", "blog.views.vprasanje"),
   url("prva.html", "blog.views.prva_stran"),
   url("lepsa.html", "blog.views.lepsa_stran"),
   url("domaca.html", "blog.views.domaca_stran"),
   url("blog.html", "blog.views.blog_stran"),
   url("galerija.html", "blog.views.galerija_stran"),
   url("onas.html", "blog.views.onas_stran"),
   url("kontakti.html", "blog.views.kontakti_stran"),
   url(r'^admin/', include(admin.site.urls)),
]


