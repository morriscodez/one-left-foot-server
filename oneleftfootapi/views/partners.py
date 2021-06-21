from django.db.models.fields import PositiveSmallIntegerField
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import Partner, DanceUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class PartnerView(ViewSet):

    def create(self, request):

        partnership = Partner()
        leader = DanceUser.objects.get(pk=request.data["leaderId"])
        follower = DanceUser.objects.get(pk=request.data["followerId"])
        
        partnership.leader = leader
        partnership.follower = follower
        

        try:
            partnership.save()
            serializer = PartnerSerializer(partnership, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as ex:
            return Response({"reason": "Already practice partners"}, status=status.HTTP_400_BAD_REQUEST) 

    
    def list(self, request):

        partnerships = Partner.objects.all()

        serializer = PartnerSerializer(
            partnerships, many=True, context={'request': request}
        )
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        try:
            partnership = Partner.objects.get(pk=pk)
            
            serializer = PartnerSerializer(partnership, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        partnership = Partner.objects.get(pk=pk)
        leader = DanceUser.objects.get(pk=request.data["leaderId"])
        follower = DanceUser.objects.get(pk=request.data["followerId"])
        
        partnership.leader = leader
        partnership.follower = follower
        
        partnership.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            partnership = Partner.objects.get(pk=pk)
            partnership.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Partner.DoesNotExist as ex:
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


class LeaderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'user')

class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'user')


class PartnerSerializer(serializers.ModelSerializer):
    leader = LeaderSerializer()
    follower = FollowerSerializer()

    class Meta:
        model = Partner
        fields = ('id', 'leader', 'follower')