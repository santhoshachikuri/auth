from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.


def home_page_view(request):
    return render(request,'authapp/home.html')

#decarators allowing us to add  functionality to multiple classes using single method
@login_required
def java_view(request):
    return render(request,'authapp/django.html')
@login_required
def python_view(request):
    return render(request,'authapp/python.html')
@login_required
def aptitude_view(request):
    return render(request,'authapp/restapi.html')

def logout_view(request):
    return render(request,'authapp/logout.html')
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form':form})