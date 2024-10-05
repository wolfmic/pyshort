"""
Main View
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views import View
from shortenerapp.models import RedirectionLink
from . import hashids
from . import logger


class ShrinkLink(View):
    """
    Main Class to shrink URL and display shortened url
    """

    def get(self, request, **kwargs):
        """
        Show URL Shortener form
        """

        myhash = kwargs.get("myhash")
        print(myhash)
        if not myhash:
            return render(request, "short.html", {})

        r = ""
        try:
            r = RedirectionLink.objects.get(hash_link=myhash)
        except RedirectionLink.DoesNotExist as e:
            logger.warning(e)

        if not r:
            HttpResponse("hash does not exist")
        return HttpResponseRedirect(r.original_link)

    def post(self, request):
        """
        Post and show URL shortened
        """
        validate = URLValidator()
        original_url = request.POST.get("original_url")
        try:
            validate(original_url)
        except ValidationError as e:
            logger.critical(e)
            return render(request, "short.html", {"hash_link": "return a valid URL"})

        new = RedirectionLink()
        new.original_link = request.POST.get("original_url")
        new.save()

        hashid = hashids.encode(new.id)
        logger.info("New hash: %s", hashid)
        new.hash_link = hashid
        new.save()

        return render(request, "short.html", {"shortened_link": new.hash_link})
