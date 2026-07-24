from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .views import DashboardHomeView, DashboardProjectCreateView, DashboardProfileUpdateView, DashboardProjectListView, DashboardProjectUpdateView, DashboardProjectDeleteView, DashboardProjectDetailView
from .views_education import *
from .views_certifications import *
from .views_contact import ContactListView, ContactResolveView
from .views_social_links import *

app_name = 'dashboard'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('', DashboardHomeView.as_view(), name='home'),
    path('projects/', DashboardProjectListView.as_view(), name='project_list'),
    path('projects/create/', DashboardProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', DashboardProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/edit/', DashboardProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', DashboardProjectDeleteView.as_view(), name='project_delete'),
    path('profile/edit/', DashboardProfileUpdateView.as_view(), name='profile_edit'),
    # Education URLs
    path('education/', EducationListView.as_view(), name='education_list'),
    path('education/create/', EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),
    path('education/<int:pk>/edit/', EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
    # Certifications URLs
    path('certifications/', CertificationListView.as_view(), name='certification_list'),
    path('certifications/create/', CertificationCreateView.as_view(), name='certification_create'),
    path('certifications/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),
    path('certifications/<int:pk>/edit/', CertificationUpdateView.as_view(), name='certification_update'),
    path('certifications/<int:pk>/delete/', CertificationDeleteView.as_view(), name='certification_delete'),
    # Contact URLs
    path('contact/', ContactListView.as_view(), name='contact_list'),
    path('contact/<int:pk>/resolve/', ContactResolveView.as_view(), name='contact_resolve'),
    # Social Links URLs
    path('social-links/', SocialLinkListView.as_view(), name='social_links_list'),
    path('social-links/create/', SocialLinkCreateView.as_view(), name='social_link_create'),
    path('social-links/<int:pk>/', SocialLinkDetailView.as_view(), name='social_link_detail'),
    path('social-links/<int:pk>/edit/', SocialLinkUpdateView.as_view(), name='social_link_update'),
    path('social-links/<int:pk>/delete/', SocialLinkDeleteView.as_view(), name='social_link_delete'),
]
