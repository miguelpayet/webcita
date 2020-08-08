from django.shortcuts import render


def admin_index(request):
    context = {}
    response = render(request, 'admin_app/index.html', context)
    return response
