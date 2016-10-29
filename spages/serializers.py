# -*- coding: utf-8 -*-

from rest_framework import serializers
from spages.models import SPage


class SPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPage
        fields = read_only_fields = ["content", "title"]