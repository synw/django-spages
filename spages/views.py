# -*- coding: utf-8 -*-

from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from spages.serializers import SPageSerializer
from spages.models import SPage


class SPageView(TemplateView):
    template_name = "spages/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(SPageView, self).get_context_data(**kwargs)
        url = self.kwargs['url']
        if not url.startswith('/'):
            url = "/"+url
        context['page'] = get_object_or_404(SPage, url=url, published=True)
        return context


class HomeSPageView(TemplateView):
    template_name = "spages/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeSPageView, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(SPage, url="/", published=True)
        return context


class SPageRestView(APIView):
    
    def get_object(self, id):
        try:
            return get_object_or_404(SPage, pk=self.kwargs['pk'], published=True)
        except SPage.DoesNotExist:
            raise Http404
    
    def get(self, request, *args, **kwargs):
        page = self.get_object(id)
        serializer = SPageSerializer(page)
        return Response(serializer.data)
    
    def get_queryset(self, *args, **kwargs):
        q = SPage.objects.filter(pk=self.kwargs['pk'], published=True)
        return q