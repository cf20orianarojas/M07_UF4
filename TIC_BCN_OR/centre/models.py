from django.db import models

# model usuari
class User(models.Model):
    nom = models.CharField(max_length = 20)
    cognom = models.CharField(max_length = 20)
    cognom2 = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    rol = models.CharField(default='default', max_length = 20)
    curs = models.CharField(max_length = 20)
    moduls = models.CharField(max_length = 20)