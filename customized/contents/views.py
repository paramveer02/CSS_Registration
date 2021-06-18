from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def reg(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('Username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('admin')


    else:
        form=UserRegistrationForm()

    return render(request,'contents/index.html',{'form':form})

