from django.shortcuts import redirect, render
from django.utils.translation import activate
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request , 'SlideShow/home.html')

def change_lang(request):
    activate(request.GET.get('lang'))
    return redirect(request.GET.get('next'))

def logout_view(request):
    logout(request)
    return redirect(request.GET.get('next'))