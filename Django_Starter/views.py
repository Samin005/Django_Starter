from django.shortcuts import redirect

redirect_url = ''


def redirect_to_app(request):
    return redirect(redirect_url)
