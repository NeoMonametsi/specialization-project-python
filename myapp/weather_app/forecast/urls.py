from django.urls import path
from .views import index
from .views import feedback_view
from .views import HomeView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import register, login_view
from .views import success_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', include('django.contrib.auth.urls')),
    path('feedback/',feedback_view, name='feedback'),
    path('',HomeView.as_view(), name='index.html'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('success/', success_view, name='success_url'),
]
