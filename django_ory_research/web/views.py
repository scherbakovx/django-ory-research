import requests

from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.conf import settings


def index(request):
    """Home page."""

    response = requests.get(
        f"{settings.ORY_SDK_URL}/sessions/whoami",
        cookies=request.COOKIES
    )
    active = response.json().get('active')
    if not active:
        return HttpResponse("You are not active")

    email = response.json().get('identity', {}).get('traits', {}).get('email').replace('@', '')

    return HttpResponse(f"You're email is {email}")
