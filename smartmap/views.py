from django.shortcuts import render
from django.conf import settings


def smartmap(request):
    context = {
        'KEY_MAP_API': settings.KEY_MAP_API
    }
    return render(request, "smartmap.html", context)
