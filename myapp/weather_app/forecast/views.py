import requests
from django.shortcuts import render
from .forms import LocationForm
from .forms import FeedbackForm 
from django.views import View
from django.contrib.auth.decorators import login_required


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
# Create your views here.
