from django.shortcuts import  render
from django.http import HttpResponseRedirect
from django.conf import settings


def unsupported(request):
    
    context = {
        "next": request.path,
    }
    
    return render(request, getattr(settings, "BADBROWSER_BASE_TEMPLATE", "django_badbrowser/base.html"), context)

def ignore(request):
    response = HttpResponseRedirect(request.GET.get("next", "") or "/")
    response.set_cookie("badbrowser_ignore", "1")
    return response
