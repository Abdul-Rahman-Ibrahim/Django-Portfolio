from django.shortcuts import render
from django.views.generic import View
from datetime import datetime
from .models import About


class HomeView(View):
    def get(self, request):
        author = About.objects.all()[0]
        user = author.user
        first_name = user.first_name
        last_name = user.last_name
        titles = author.title.split(',')
        bio = author.bio
        profile_image = author.profile_image
        location = author.location
        email = author.email
        twitter_url = author.twitter_url
        github_url = author.github_url

        current_year = datetime.now().year

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'titles': titles,
            'bio': bio,
            'profile_image': profile_image,
            'location': location,
            'email': email,
            'twitter_url': twitter_url,
            'github_url': github_url,
            'current_year': current_year,
        }

        print(author)
        return render(request, 'index.html', context=context)


class ResumeView(View):
    def get(self, request):
        return render(request, 'resume.html')


class ProjectsView(View):
    def get(self, request):
        return render(request, 'projects.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')