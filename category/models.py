from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=55)

    def __str__(self):
        return f"Category name: {self.categoryName}"