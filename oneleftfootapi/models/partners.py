from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

class Partner(models.Model):

    leader = models.ForeignKey("DanceUser", on_delete=CASCADE, related_name="leader")
    follower = models.ForeignKey("DanceUser", on_delete=CASCADE, related_name='follower')

    # An instance of
    class Meta:
        unique_together = ("leader", "follower")