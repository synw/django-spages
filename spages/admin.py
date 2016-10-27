# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from spages.models import SPage


@admin.register(SPage)
class SPageAdmin(MPTTModelAdmin):
    #form = PageAdminForm
    date_hierarchy = 'edited'
    search_fields = ['title','url','editor__username']
    list_display = ['url','title','published','edited','editor']
    list_select_related = ['editor']
    list_display_links = ['title','url']
    list_filter = ['created','edited','published']
    list_select_related = ['editor']
    mptt_level_indent = 25