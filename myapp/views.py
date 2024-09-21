from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ProfileForm
from django.contrib.auth import login,logout as authlogout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . models import UserProfile

# Create your views here.

@login_required(login_url='login')
def createpage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)  # Don't save to the database yet
            profile.user = request.user  # Associate the profile with the current user
            profile.save()
    else: 
        form = ProfileForm()  # Initialize the form for a GET request

    return render(request, 'create.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view or URL pattern
        
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    
    return render(request, 'loginpage.html')

def homepage(request):
    user_profile_exists = False
    if request.user.is_authenticated:
        user_profile_exists = UserProfile.objects.filter(user=request.user).exists()
    print(user_profile_exists)
    return render(request, 'home.html', {'user_profile_exists': user_profile_exists})

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        if c_password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
    
    return render(request, 'register.html')


@login_required(login_url='login')
def profilepage(request):
    user_set=UserProfile.objects.get(user=request.user)
    return render(request,'profile.html',{'user':user_set})

def logoutprofile(request):
    authlogout(request)  # Logs out the user
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirects to the login page


@login_required(login_url='login')
def updatepage(request):
    user_set=UserProfile.objects.get(user=request.user)
    if request.method == 'POST': 
        form = ProfileForm(request.POST,request.FILES,instance=user_set)
        if form.is_valid():
            profile = form.save(commit=False)  # Don't save to the database yet
            profile.user = request.user  # Associate the profile with the current user
            profile.save()
    else: 
        form = ProfileForm(instance=user_set)  # Initialize the form for a GET request

    return render(request, 'update.html', {'form': form})

