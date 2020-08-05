import json
from django.conf import settings
from django.http import HttpResponse


def root(request):
    return HttpResponse(json.dumps({'OCFL REPO': {'root': settings.OCFL_STORAGE_ROOT}}))
