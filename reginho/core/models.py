from django.db import models

# Create your models here.

class Regi(models.Model):

    materias = (
        ('mat', 'matematica'),
        ('fis', 'fisica'),
        ('bio', 'biologia'),
        ('qui', 'quimica')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    conter = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    materia = models.CharField(
        max_length=15,
        choices=materias,
    )