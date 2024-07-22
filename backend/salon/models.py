from django.db import models
from django.conf import settings
# Create your models here.

class Salon(models.Model):
    # Assuming a Salon has a name and description
    
    name = models.CharField(max_length=40)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    layout = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Post(models.Model):
    # Foreign key to the salon this post belongs to
    salon = models.ForeignKey(Salon, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    # Foreign key to the salon this assignment belongs to
    salon = models.ForeignKey(Salon, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
