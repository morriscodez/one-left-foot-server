from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

class Availability(models.Model):

    dance_user = models.ForeignKey("DanceUser", on_delete=CASCADE)
    day = models.ForeignKey("Day", on_delete=CASCADE)
    start = models.TimeField
    end = models.TimeField