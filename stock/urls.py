# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:26:41 2016

@author: cliente
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # /stock/
    url(r'^$', views.index, name='index'),

    # /stock/stock.id/
    url(r'^(?P<stock_id>[0-9]+)/$', views.detail, name='detail'),
]

