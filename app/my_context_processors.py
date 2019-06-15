from django.conf import settings


def settings_context_processor(request):
    settings_dict = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return settings_dict
