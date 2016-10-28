# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from spages.models import SPage
from spages.forms import SPageAdminForm


@admin.register(SPage)
class SPageAdmin(MPTTModelAdmin):
    form = SPageAdminForm
    date_hierarchy = 'edited'
    search_fields = ['title','url','editor__username']
    list_display = ['url','title','published','edited','editor']
    list_select_related = ['editor']
    list_display_links = ['title','url']
    list_filter = ['created','edited','published']
    list_select_related = ['editor']
    mptt_level_indent = 25
    
    def get_fieldsets(self, request, obj=None):
        super(SPageAdmin, self).get_fieldsets(request, obj)
        base_fields = (('url', 'parent'),'title', 'template_name','published')
        fieldsets = (
            (None, {
                'fields': ('content',)
            }),
            (None, {
                'fields': base_fields,
            }),
            (_(u'SEO'), {
                'classes': ('collapse',),
                'fields': ('seo_keywords','seo_description')
            }),
        )
        return fieldsets