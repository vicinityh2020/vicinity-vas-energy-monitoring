from django.http import JsonResponse
from django.conf import settings


# Create your views here.
def thing_description(request):
    return JsonResponse(settings.THING_DESCRIPTION)
