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

    
    @property
    def already_follower(self):
        return self.__already_follower

    @already_follower.setter
    def already_follower(self, value):  
        self.__already_follower = value
    
    
    @property
    def already_leader(self):
        return self.__already_leader

    @already_leader.setter
    def already_leader(self, value):  
        self.__already_leader = value


    @property
    def pending_request(self):
        return self.__pending_request

    @pending_request.setter
    def pending_request(self, value):
        self.__pending_request = value