from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ResumeView(View):
    def get(self, request):
        return render(request, 'resume.html')


class ProjectsView(View):
    def get(self, request):
        return render(request, 'projects.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')