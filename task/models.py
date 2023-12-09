from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    categories = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    # taskAssignedDate = models.DateField()
    taskAssignedDate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Title: {self.taskTitle}"