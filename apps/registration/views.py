# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('register')

    return render(request, 'registration/register.html')
