from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import related

class Partners(models.Model):

    leader = models.ForeignKey("DanceUser", on_delete=CASCADE, related_name="leader")
    follower = models.ForeignKey("DanceUser", on_delete=CASCADE, related_name='follower')