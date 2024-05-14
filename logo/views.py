from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registraion/register.html'
    success_url = reverse_lazy('login')


def log(request):
    obj=User.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user=request.user
            id=current_user.id
            return redirect('frontpage')
    return render(request,'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('frontpage')


