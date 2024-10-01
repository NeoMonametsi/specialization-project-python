import requests
from django.shortcuts import render,redirect
from .forms import LocationForm
from .forms import FeedbackForm 
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
def get_weather_data(location):
    api_key = 'd0b04578a68adad4daf401c3c34ea27c'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def index(request):
    weather = {}
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            weather = get_weather_data(location)

    return render(request, 'forecast/index.html', {'form': form, 'weather': weather})

@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Optional
            feedback.save()
            return redirect('success_url')  # Redirect after saving

    else:
        form = FeedbackForm()
    return render(request, 'forecast/feedback.html', {'form': form})


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')

    return render(request, 'register.html')
                        
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or another page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def success_view(request):
    return render(request, 'success.html') 
# Create your views here.
