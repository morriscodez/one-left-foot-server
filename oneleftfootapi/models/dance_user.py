from django.db import models
from django.contrib.auth.models import User


class DanceUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    img = models.ImageField(upload_to="One-Left-Foot")

    @property
    def requests(self):
        return self.__requests

    @requests.setter
    def requests(self, value):
        self.__requests = value
