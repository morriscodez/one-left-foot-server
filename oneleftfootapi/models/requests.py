from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import related

class Request(models.Model):

    sender = models.ForeignKey("DanceUser", on_delete=CASCADE, related_name='sender')
    receiver = models.ForeignKey("DanceUser", on_delete=CASCADE, related_name='receiver')