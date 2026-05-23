from django.urls import path
from .views import DashboardHomeView, DashboardProjectCreateView
app_name = 'dashboard'
urlpatterns = [path('', DashboardHomeView.as_view(), name='home'), path('projects/create/', DashboardProjectCreateView.as_view(), name='project_create')]
