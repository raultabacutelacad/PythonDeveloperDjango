from django.db import models

# Create your models here.
from django.db import models

class Carte(models.Model):
    titlu = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    descriere = models.TextField()

    def __str__(self):
        return self.titlu