from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        l_username=request.POST['username']
        l_password=request.POST['password']
        party2=auth.authenticate(username=l_username,password=l_password)

        if party2 is not None:
            auth.login(request,party2)
            return redirect('/')
        else:
            messages.info(request,"invalid ")
            return redirect('login')



    return render(request,"login.html")
        
def register(request):
     if request.method=='POST':
          username1=  request.POST['username']
          firstname =  request.POST['first_name']
          last_name = request.POST['last_name']
          email = request.POST['email']
          password = request.POST['password']
          if User.objects.filter(username=username1).exists():
               messages.info(request,"username is already taken")
               print("due to existing username user not created")
               return redirect('register')

          elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already exists")
                print("due to existing email user not created")
                return redirect('register')
          else:
                party=User.objects.create_user(username=username1,first_name=firstname,last_name=last_name,email=email,password=password)
                party.save();
                return redirect('login')
                print("user created")
     return render(request,"register.html")
def logout(request):
     auth.logout(request)
     return redirect('/')