from django.urls import path
from .views import HomeView, RobotsView
app_name = 'portfolio'
urlpatterns = [path('', HomeView.as_view(), name='home'), path('robots.txt', RobotsView.as_view(), name='robots')]
