from django.db import models

class Days(models.Model):

    day = models.CharField(max_length=7)