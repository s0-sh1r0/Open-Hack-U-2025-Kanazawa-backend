from django.db import models
from django.contrib.auth.models import User # Django標準のUserモデル

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_access_token = models.CharField(max_length=255, blank=True, null=True, verbose_name="GitHub Access Token")
    openai_api_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="OpenAI API Key")

    def __str__(self):
        return self.user.username
    