from django.db import models

class DanceType(models.Model):

    label = models.CharField(max_length=25)