from django.db import models
from  django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.TextField(max_length=500, blank=True)
    Image = models.ImageField(upload_to='profile_pics', blank=True)
    CreatedJobs = models.ForeignKey('Jobs', on_delete=models.CASCADE, null=True)
    CompletedWork = models.ForeignKey('Jobs', on_delete=models.CASCADE, null=True)
    ListChats = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)

class Jobs(models.Model):
    Creator = models.ForeignKey("Profile", on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description  = models.TextField(max_length=500)
    Category  = models.CharField(max_length=100)
    File = models.FileField(upload_to='job_files')
    Created  = models.DateTimeField(auto_now_add=True)
    Completed= models.DateTimeField(null=True)
    CompletedBy  = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    Image = models.ImageField(upload_to='job_pics', blank=True)
    Reward  = models.IntegerField(default=0)
    Status   = models.CharField(max_length=100, default='Pending')
    Chat  = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)

class Chats(models.Model):
    Job = models.ForeignKey('Jobs', on_delete=models.CASCADE, null=True)
    ListUsers  = models.ForeignKey('Profile', on_delete=models.CASCADE)
    Messages   = models.ForeignKey('Messages', on_delete=models.CASCADE, null=True)
    Image  = models.ImageField(upload_to='chat_pics', blank=True)
    Created   = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100)

class Messages(models.Model):
    Sender  = models.ForeignKey('Profile', on_delete=models.CASCADE)
    Chat  = models.ForeignKey('Chats', on_delete=models.CASCADE)
    Text   = models.TextField(max_length=500)
    Image   = models.ImageField(upload_to='chat_pics', blank=True)
    Created   = models.DateTimeField(auto_now_add=True)
    File    = models.FileField(upload_to='chat_files', blank=True)
