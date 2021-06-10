from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import DanceUser
from django.contrib.auth.models import User




class DanceUserView(ViewSet):

    def list(self, request):

        dance_users = DanceUser.objects.get.all()

        serializer = DanceUserSerializer(
            dance_users, many=True, context={'request': request}
        )
        return Response(serializer.data)



class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class DanceUserSerializer(serializers.Serializer):

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'img')

