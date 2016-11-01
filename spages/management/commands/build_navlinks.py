# -*- coding: utf-8 -*-

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from spages.models import SPage
from django.core.urlresolvers import reverse


class Command(BaseCommand):
    help = 'Build navigation links for spages'

    def handle(self, *args, **options):
        pages = SPage.objects.filter(level=1, published=True)
        print "Building navigation ..."
        navlinks = []
        i = 1
        for page in pages:
            url = reverse("spages-page", kwargs={'url':page.url})
            val = '<li><a class="btn btn-link" href="'+url.replace("%2F", "")+'">'+page.title+'</a></li>'
            navlinks.append(val)
            print str(i)+": "+page.url
            i += 1
        navlinks_str = '\n'.join(navlinks)
        # check directories
        dirpath = settings.BASE_DIR+"/templates/spages"
        if not os.path.isdir(dirpath) is True:
            print "Creating directory templates/spages"
            os.makedirs(dirpath)
        dirpath = settings.BASE_DIR+"/templates/spages/auto"
        if not os.path.isdir(dirpath) is True:
            os.makedirs(dirpath)
            print "Creating directory templates/spages/auto"
        # update
        filepath=settings.BASE_DIR+"/templates/spages/auto/navlinks.html"
        print "Updating templates/spages/auto/navlinks.html"
        #~ write the file
        filex = open(filepath, "w")
        filex.write(navlinks_str)
        filex.close()
        print "OK: "+str(i-1)+" navlinks built"
        return