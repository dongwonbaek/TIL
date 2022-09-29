from email.policy import default
from pyexpat import model
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=10, default="할일")
    content = models.CharField(max_length=80)
    priority = models.IntegerField(default=3)
    completed = models.BooleanField(default=False)
    # default(기본값): 데이터를 생성할 때 값을 넣지않으면 기본값으로 생성한다.
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
