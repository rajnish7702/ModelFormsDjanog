from django.db import models

# Create your models here.

class GeeksModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    rollnum = models.IntegerField()
    collegeName = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name