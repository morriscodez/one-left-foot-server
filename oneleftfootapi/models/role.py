from django.db import models

class Role(models.Model):

    label = models.CharField(max_length=8)