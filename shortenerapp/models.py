"""
Shortener App Models
"""

from django.db import models


class RedirectionLink(models.Model):
    """
    RediractionLink class
    """

    original_link = models.URLField()
    hash_link = models.CharField(max_length=8)
    creation_date = models.DateTimeField(auto_now_add=True)
