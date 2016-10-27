# -*- coding: utf-8 -*-

from django.conf.urls import url
from spages.views import SPageView, HomeSPageView, SPageRestView


urlpatterns = [
    url(r'^rest/(?P<pk>[0-9]+)/$', SPageRestView.as_view(), name="spages-rest"),
    url(r'^(?P<url>.*?)$', SPageView.as_view(), name="spages-page"),
    url(r'^', HomeSPageView.as_view(), name="spages-home"),
    ]