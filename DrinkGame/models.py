from django.db import models

# Create your models here.
class Card(models.Model):
    #add author
    body = models.TextField()

    def __str__(self):
        return self.body