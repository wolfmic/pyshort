"""
Shortener App
"""

import logging
from hashids import Hashids
from django.conf import settings

logger = logging.getLogger(__name__)
hashids = Hashids(min_length=4, salt=settings.SECRET_KEY)
