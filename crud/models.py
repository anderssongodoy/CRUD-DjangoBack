from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title