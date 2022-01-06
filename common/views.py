from django.http import JsonResponse


def app_info(request):
    response = {
        'name': 'Projectile',
        'info': 'A simple REST API Project',
        'version': '0.0.3',
    }
    return JsonResponse(response)
