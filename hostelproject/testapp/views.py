from django.shortcuts import render
from testapp.forms import SignUpForm,RegisterForm
from django.http import HttpResponseRedirect
from testapp.models import Register


# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def hotels_view(request):
    return render(request,'testapp/hotels.html')

def cruise_view(request):
    return render(request,'testapp/cruise.html')


def travel_view(request):
    return render(request,'testapp/travel.html')


def contact_view(request):
    return render(request,'testapp/contact.html')

def logth_view(request):
    return render(request, 'testapp/logth.html')


def logout_view(request):
    return render(request, 'testapp/logout.html')


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})



def register_view(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thankspage')
    return render(request,'testapp/registerform.html',{'form':form})

def thanks_view(request):
    return render(request,'testapp/thankspage.html')
