from django.shortcuts import render,redirect,get_object_or_404
from web.models import Flan, Gelatina
from .forms import ContactForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


def index(request):
    flanes_publicos =Flan.objects.filter(is_private=False)
    return render(request,'index.html',{'flanes':flanes_publicos})


def about(request):
    return render(request,'about.html',{})

@login_required
def welcome(request):
    flanes_privados =Flan.objects.filter(is_private=True)
    gelatina_privados =Gelatina.objects.filter(is_private=True)
    return render (request,'welcome.html',{'flanes':flanes_privados,'gelatinas':gelatina_privados})



def contact_view(request):      #esto recordaro
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exitoso')
    else:
        form=ContactForm()
    return render(request,'contact_form.html',{'form':form})

def contact_view_exito(request):
    return render(request,'contacto_exitoso.html',{})



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


# class CustomLogoutView(LogoutView):
#     next_page = '/'

def logout_view(request):
    logout(request)
    return render(request,'registration/logout.html')



def flan_details(request, flan_id):
    flan = get_object_or_404(Flan,pk=flan_id)
    return render(request,'flan_details.html',{'flan':flan})

def gelatina(request):
    gelatina_publicos =Gelatina.objects.filter(is_private=False)
    return render(request,'gelatina.html',{'gelatinas':gelatina_publicos})


def gelatina_details(request, gelatina_id):
    gelatina = get_object_or_404(Gelatina,pk=gelatina_id)
    return render(request,'gelatina_details.html',{'gelatina':gelatina})
