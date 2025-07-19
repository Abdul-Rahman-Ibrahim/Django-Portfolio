from django.urls import path
from .views import HomeView, ResumeView, ProjectsView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]