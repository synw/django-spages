# -*- coding: utf-8 -*-

from django.core.management import call_command
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel
from spages.conf import USER_MODEL


class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, blank=True, verbose_name=_(u'SEO: description'), help_text=_(u'Short description of the page content'))
    seo_keywords = models.CharField(max_length=120, null=True, blank=True, verbose_name=_(u'SEO: keywords'), help_text=_(u'List of keywords separated by commas'))

    class Meta:
        abstract = True
        verbose_name=_(u'SEO')


class SPage(MPTTModel, Seo):
    url = models.CharField(_(u'Url'), max_length=180, db_index=True)
    title = models.CharField(_(u'Title'), max_length=200)
    content = models.TextField(_(u'Content'), blank=True)
    template_name = models.CharField(_(u'Template name'), max_length=120, blank=True,
        help_text=_(u'If no template name is provided "spages/index.html" will be used.')
    )
    parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children', verbose_name=_(u'Parent page'))
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True, verbose_name=_(u'Created'))
    editor = models.ForeignKey(USER_MODEL, editable = False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   
    published = models.BooleanField(default=True, verbose_name=_(u'Published'))
    
    class Meta:
        verbose_name = _(u'Page')
        verbose_name_plural = _(u'Page')
        ordering = ['url']
        
    def get_absolute_url(self):
        return self.url
    
    def __unicode__(self):
        return unicode(self.title)
    
    def update_routes(self):
        call_command('build_routes', verbosity=0)
        return
    
    def delete(self, *args, **kwargs):
        super(SPage, self).delete(*args, **kwargs)
        self.update_routes()
        return
    
    def save(self, *args, **kwargs):
        super(SPage, self).save(*args, **kwargs)
        self.update_routes()
        return