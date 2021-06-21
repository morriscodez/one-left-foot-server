from django.db.models.fields import PositiveSmallIntegerField
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import Availability, DanceUser, Day
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.decorators import action
import datetime


class AvailabilityView(ViewSet):

    def create(self, request):

        window = Availability()
        dancer = DanceUser.objects.get(user=request.auth.user)
        day = Day.objects.get(pk=request.data["dayId"])
        
        window.start = request.data["start"]
        window.end = request.data["end"]
        window.dance_user = dancer
        window.day = day
        
        start_time_object = datetime.datetime.strptime(window.start, '%H:%M').time()
        end_time_object = datetime.datetime.strptime(window.end, '%H:%M').time()

        try:
            
            todays_availabilities = dancer.availability_set.filter(day=day)

            for availability_window in todays_availabilities:
                if start_time_object >= availability_window.start and start_time_object <= availability_window.end:

                    return Response({"reason": "Overlapping availability range."}, status=status.HTTP_400_BAD_REQUEST)

                if end_time_object >= availability_window.start and end_time_object <= availability_window.end:

                    return Response({"reason": "Overlapping availability range."}, status=status.HTTP_400_BAD_REQUEST)
            
            window.save()
            serializer = AvailabilitySerializer(window, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):

        windows = Availability.objects.all()

        
        serializer = AvailabilitySerializer(
            windows, many=True, context={'request': request}
        )
        return Response(serializer.data)

    
    @action(methods=['get'], detail=False)
    def myavailability(self, request, pk=None):
        
        if request.method == "GET":
            windows = Availability.objects.filter(dance_user__id=request.auth.user.id)

        try:
            serializer = AvailabilitySerializer(
                windows, many=True, context={'request': request}
                )
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def retrieve(self, request, pk=None):
        try:
            window = Availability.objects.get(pk=pk)
            
            serializer = AvailabilitySerializer(window, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        window = Availability.objects.get(pk=pk)
        dancer = DanceUser.objects.get(pk=request.data["danceUserId"])
        day = Day.objects.get(pk=request.data["dayId"])
        
        window.start = request.data["start"]
        window.end = request.data["end"]
        window.dance_user = dancer
        window.day = day
        
        window.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            window = Availability.objects.get(pk=pk)
            window.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Availability.DoesNotExist as ex:
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

class AvailabilitySerializer(serializers.ModelSerializer):
    dance_user = DanceUserSerializer()

    class Meta:
        model = Availability
        fields = ('id', 'dance_user', 'day', 'start', 'end')
        depth = 1