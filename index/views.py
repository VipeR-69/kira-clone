from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib import auth

@csrf_exempt
def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used by another account, please use a different email')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken, please use different username')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return render(request, 'login.html')
    
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('signup')
    
    else:
        return render(request, 'signup.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        test = auth.authenticate(username=username, password=password)
        if test is not None:
            auth.login(request, test)
            return redirect("home")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')