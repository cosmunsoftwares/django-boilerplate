from django.conf import settings


def debug(request):

    context = {
        'DEBUG': settings.DEBUG,
    }

    return context
