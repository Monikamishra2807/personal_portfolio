from django.urls import path
from .views import HomeView, AboutView, RobotsView, Custom404View, Custom403View, Custom500View

app_name = 'portfolio'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
    path('404/', Custom404View.as_view(), name='404'),
    path('403/', Custom403View.as_view(), name='403'),
    path('500/', Custom500View.as_view(), name='500'),
]
