from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import Day
from django.core.exceptions import ValidationError


class DayView(ViewSet):

    
    def list(self, request):

        days = Day.objects.all()

        serializer = DaySerializer(
            days, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        try:
            day = Day.objects.get(pk=pk)
            
            serializer = DaySerializer(day, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)



class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = ('id', 'day')