from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
