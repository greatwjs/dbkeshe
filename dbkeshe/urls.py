"""dbkeshe URL Configuration

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
from mainsite.views import login,logout,zhuce,playif,luruscore,tijiao,chaxun,chaxun1,chaxun2,chaxun4,chaxun3

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$|login$',login),
    url(r'^login/zhuce|zhuce$',zhuce),
    url(r'^$',playif),
    url(r'^chaxun/score|score/score|score/$',luruscore),
    url(r'^tijiao$',tijiao),
    url(r'^score/chaxun$|chaxun/$',chaxun),
    url(r'^chaxun1$',chaxun1),
    url(r'^chaxun2$',chaxun2),
    url(r'^chaxun4/|score/chaxun4$|chaxun/chaxun4',chaxun4),
    url(r'^chaxun3$',chaxun3),
    url(r'^logout$',logout),
]
