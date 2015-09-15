# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^auth/login', views.login, name='login'),
    url('^auth/logout', views.logout, name='logout'),
    url('^offers/list$', views.list_offers, name='list_offers'),
    url('^offers/activate/(?P<offer_id>[0-9]+)$', views.activate_offer, name='activate_offer'),
    url('^offers/show/(?P<offer_id>[0-9]+)$', views.show_offer, name='show_offer'),
    url(r'^page/(?P<template_name>[\w-]+)$', views.static_pages, name='static_page'),
]
