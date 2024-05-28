from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    #add author
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Session(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_players = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session for {self.user.username}"

class Player(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.points} points"
