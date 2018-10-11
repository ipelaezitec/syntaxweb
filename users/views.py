from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada! Puedes iniciar sesión')
            return redirect('login')
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()

    return render(request,'users/register.html',{'form':form})

