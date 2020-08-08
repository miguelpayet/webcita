from django.middleware.locale import LocaleMiddleware


class MiLocaleMiddleware(LocaleMiddleware):

    def process_request(self, request):
        request.META['HTTP_ACCEPT_LANGUAGE'] = 'es-pe'
        super().process_request(request)
