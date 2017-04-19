"""practica1 URL Configuration

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
from django.contrib.auth.views import login, logout

from booksList.views import mainpage, dashboard

urlpatterns = [
    # El + es una vez o mas
    # [a-zA-Z0-9]+ --> \w+ quiere decir que no este en blanco
    # \w+.\w+ una palabra.otrapalabra
    url(r'^$', mainpage),
    url(r'^bookslist/(\w+)/$', dashboard), # Entre parentesis sera un parametre
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]