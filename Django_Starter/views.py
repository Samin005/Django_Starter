from django.shortcuts import redirect
from . import settings

current_app = ''


def redirect_to_app(request):
    return redirect(settings.root_url+current_app+'/')
