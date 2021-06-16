from django.db.models.fields import PositiveSmallIntegerField
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import Request, DanceUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RequestView(ViewSet):

    def create(self, request):

        new_request = Request()
        sender = DanceUser.objects.get(user=request.auth.user)
        receiver = DanceUser.objects.get(pk=request.data["receiverId"])
        
        new_request.sender = sender
        new_request.receiver = receiver
        
        

        try:
            new_request.save()
            serializer = RequestSerializer(new_request, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):

        new_requests = Request.objects.all()

        serializer = RequestSerializer(
            new_requests, many=True, context={'request': request}
        )
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        try:
            new_request = Request.objects.get(pk=pk)
            
            serializer = RequestSerializer(new_request, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        new_request = Request.objects.get(pk=pk)
        sender = DanceUser.objects.get(pk=request.data["senderId"])
        receiver = DanceUser.objects.get(pk=request.data["receiverId"])
        
        new_request.sender = sender
        new_request.receiver = receiver
        
        new_request.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            new_request = Request.objects.get(pk=pk)
            new_request.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Request.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class DanceUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'user')


class RequestSerializer(serializers.ModelSerializer):
    sender = DanceUserSerializer()
    receiver = DanceUserSerializer()

    class Meta:
        model = Request
        fields = ('id', 'sender', 'receiver')