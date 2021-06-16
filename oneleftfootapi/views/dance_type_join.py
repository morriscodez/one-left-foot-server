from oneleftfootapi.views.dance_type import DanceTypeSerializer
from django.db.models.fields import PositiveSmallIntegerField
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import DanceTypeJoin, DanceUser, DanceType, SkillLevel, Role
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class DanceTypeJoinView(ViewSet):

    def create(self, request):

        new_dance = DanceTypeJoin()
        dancer = DanceUser.objects.get(pk=request.data["danceUserId"])
        type = DanceType().objects.get(pk=request.data["danceTypeId"])
        skill = SkillLevel.objects.get(pk=request.data["skillLevelId"])
        role = Role.objects.get(pk=request.data["roleId"])

        new_dance.dance_user = dancer
        new_dance.dance_type = type
        new_dance.skill_level = skill
        new_dance.role = role

        try:
            new_dance.save()
            serializer = DanceTypeJoinSerializer(new_dance, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):

        my_dances = DanceTypeJoin.objects.filter(dance_user__id=request.auth.user.id)

        serializer = DanceTypeJoinSerializer(
            my_dances, many=True, context={'request': request}
        )
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        try:
            my_dances = DanceTypeJoin.objects.filter(dance_user__id=pk)
            
            serializer = DanceTypeJoinSerializer(my_dances, many=True, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        new_dance = DanceTypeJoin.objects.get(pk=pk)
        
        dancer = DanceUser.objects.get(pk=request.data["danceUserId"])
        type = DanceType.objects.get(pk=request.data["danceTypeId"])
        skill = SkillLevel.objects.get(pk=request.data["skillLevelId"])
        role = Role.objects.get(pk=request.data["roleId"])


        new_dance.dance_user = dancer
        new_dance.dance_type = type
        new_dance.skill_level = skill
        new_dance.role = role

        
        new_dance.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            new_dance = DanceTypeJoin.objects.get(pk=pk)
            new_dance.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except DanceTypeJoin.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'label')

class SkillLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillLevel
        fields = ('id', 'label')

class DanceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DanceType
        fields = ('id', 'label')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class DanceUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'user')


class DanceTypeJoinSerializer(serializers.ModelSerializer):
    dance_user = DanceUserSerializer()
    dance_type = DanceTypeSerializer()
    skill_level = SkillLevelSerializer()
    role = RoleSerializer()

    class Meta:
        model = DanceTypeJoin
        fields = ('id', 'dance_user', 'dance_type', 'skill_level', 'role')