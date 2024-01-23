# O carte are urmatoarele campuri: 
# * titlu
# * autor
# * descriere
# * citit - Boolean 
# * rating - (0-5)
# * imagini adaugate pentru o carte (extensie)

import os
from django.db import models

class Carte(models.Model):
    titlu = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descriere = models.TextField()
    citit = models.BooleanField(default=False)
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
    imagine = models.ImageField(upload_to = 'biblioteca/static/')

    def filename(self):
        return os.path.basename(self.imagine.name)