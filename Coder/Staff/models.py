from django.db import models

# Create your models here.
class Persona:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()

class Profesor(Persona, models.Model):
    pass

class Tutor(Persona, models.Model):
    pass
