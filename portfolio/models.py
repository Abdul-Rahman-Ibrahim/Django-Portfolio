from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=150, help_text="Short professional title e.g., Full Stack Developer")
    bio = models.TextField(help_text="Main About Me content")
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    cv = models.FileField(upload_to='about/cv/', blank=True, null=True, help_text="Optional CV/resume upload")
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"About - {self.user.get_full_name() or self.user.username}"
