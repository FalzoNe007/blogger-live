from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True) 
    profile_picture = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', blank=True)
    date_of_birth = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    header = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
    