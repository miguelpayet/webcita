from django.conf import settings


def settings_context_processor(request):
    settings_dict = {
        'MEDIA_URL': settings.MEDIA_URL,
        'CANONICAL_PATH': request.build_absolute_uri(request.path)
    }
    return settings_dict
