# -*- coding: utf-8 -*-

import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from spages.models import SPage
from django.core.urlresolvers import reverse


class Command(BaseCommand):
    help = 'Build routes for spages'

    def handle(self, *args, **options):
        pages = SPage.objects.filter(published=True)
        print "Building routes ..."
        routes = []
        i = 1
        for page in pages:
            rest_url = reverse("spages-rest", kwargs={'pk':page.pk})
            val = "page('"+page.url+"', function(ctx, next) { loadPage('"+rest_url+"') } );"
            routes.append(val)
            print str(i)+": "+page.url
            i += 1
        routes_str = '{% include "spages/extra_routes.js" %}\n'+'\n'.join(routes)
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
        filepath=settings.BASE_DIR+"/templates/spages/auto/routes.js"
        print "Updating templates/spages/auto/routes.js"
        #~ write the file
        filex = open(filepath, "w")
        filex.write(routes_str)
        filex.close()
        print "OK: "+str(i-1)+" routes built "
        return