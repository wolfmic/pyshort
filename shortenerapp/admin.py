"""
Shortener App Admin Registration
"""

from django.contrib import admin
from .models import RedirectionLink

class RedirectionLinkAdmin(admin.ModelAdmin):
    """
    Display Direction Link in Admin
    """
    list_display = ('original_link', 'hash_link', 'creation_date')


admin.site.register(RedirectionLink, RedirectionLinkAdmin)
