from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User #It comes default with Django


from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
     #Get Forms Values

     first_name  = request.POST['first_name']
     last_name  = request.POST['last_name']
     username  = request.POST['username']
     email  = request.POST['email']
     password  = request.POST['password']
     password2  = request.POST['password2']

     #Check whether passwrod match:

     if password == password2:
         #check username
         if User.objects.filter(username=username).exists():
             messages.error(request, 'This username exists , change it')
             return render(request,'accounts/register.html')
         else:
             if User.objects.filter(email=email).exists():
                  messages.error(request, 'This email exists , change it')
                  return render(request,'accounts/register.html')
             else:
                 #All is well, Got ehead and create the user - Saved in database
                 user = User.objects.create_user(username=username, password = password,email=email,
                 first_name= first_name, last_name = last_name)
                 #Login after register
                 #auth.login (request, user)
                 #messages.success(request,'You are now logged in')
                 #return redirect('index')

                 user.save()
                 messages.success(request,'You are now register and can log in')
                 return redirect('login')

     else:
         messages.error(request, 'Password do not match')
         return redirect('accounts/register.html')
        
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
    return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')