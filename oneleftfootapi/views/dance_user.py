from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import DanceUser, dance_user
from django.contrib.auth.models import User




class DanceUserView(ViewSet):

    def list(self, request):

        dance_users = DanceUser.objects.all()

        serializer = DanceUserSerializer(
            dance_users, many=True, context={'request': request}
        )
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        try:
            dance_user = DanceUser.objects.get(pk=pk)
            
            serializer = DanceUserSerializer(dance_user, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        
        user = DanceUser.objects.get(pk=pk)
        user.bio = request.data["bio"]
        user.img = request.data["img"]
        
        user.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            user = DanceUser.objects.get(pk=pk)
            user.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except DanceUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class DanceUserSerializer(serializers.Serializer):

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'img')

