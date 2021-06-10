from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import DanceType
from django.contrib.auth.models import User


class DanceTypeView(ViewSet):

    def list(self, request):

        dance_types = DanceType.objects.all()

        serializer = DanceTypeSerializer(
            dance_types, many=True, context={'request': request}
        )
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        try:
            dance_type = DanceType.objects.get(pk=pk)
            
            serializer = DanceTypeSerializer(dance_type, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        
        type = DanceType.objects.get(pk=pk)
        type.label = request.data["label"]
        
        type.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            type = DanceType.objects.get(pk=pk)
            type.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except DanceType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DanceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DanceType
        fields = ('id', 'label')