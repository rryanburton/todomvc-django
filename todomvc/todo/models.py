from django.db import models

# Create your models here.


class ToDo:
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)
