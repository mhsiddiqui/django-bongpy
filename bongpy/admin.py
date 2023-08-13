"""
Admin view for adding configurations
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Configuration


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_filter = ['type']
    list_display = ['key', 'value', 'group', 'is_active', 'type', 'created', 'modified']
    search_fields = ['key', 'value']
    ordering = ['-is_active']

