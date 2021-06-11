from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import SkillLevel
from django.core.exceptions import ValidationError


class SkillLevelView(ViewSet):

    def create(self, request):

        skill_level = SkillLevel()
        skill_level.label = request.data["label"]
        
        try:
            skill_level.save()
            serializer = SkillLevelSerializer(skill_level, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request):

        skill_levels = SkillLevel.objects.all()

        serializer = SkillLevelSerializer(
            skill_levels, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        try:
            skill_level = SkillLevel.objects.get(pk=pk)
            
            serializer = SkillLevelSerializer(skill_level, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        
        type = SkillLevel.objects.get(pk=pk)
        type.label = request.data["label"]
        
        type.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            type = SkillLevel.objects.get(pk=pk)
            type.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except SkillLevel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SkillLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillLevel
        fields = ('id', 'label')