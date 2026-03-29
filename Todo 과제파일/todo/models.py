from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #유저 추가

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #유저 필드 추가
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
