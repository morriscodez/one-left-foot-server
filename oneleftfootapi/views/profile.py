from oneleftfootapi.models.days import Day
from oneleftfootapi.models.partners import Partner
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import DanceUser, Partner, Request, Availability
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# from not folder => https://res.cloudinary.com/dcmrgodiq/image/upload/v1623339050/swayze_uwiqly.jpg
# from folder=> https://res.cloudinary.com/dcmrgodiq/image/upload/v1623359013/One-Left-Foot/james_lnvbjn.jpg
# from fetch db (currently)=> https://res.cloudinary.com/dcmrgodiq/image/upload/swayze_gmzgvp.jpg

class ProfileView(ViewSet):

    def list(self, request):

        try:
            dance_user = DanceUser.objects.get(user=request.auth.user)

            dance_user.availability_set.set(dance_user.availability_set.order_by('day'))

            try:
                requests = Request.objects.filter(receiver=dance_user)

                dance_user.requests = requests

            except Request.DoesNotExist as ex:
                pass

            serializer = DanceUserSerializer(dance_user, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

        

    
    def retrieve(self, request, pk=None):
        
        
        try:
            dance_user = DanceUser.objects.get(pk=pk)
            
            requests = Request.objects.filter(receiver=dance_user)

            dance_user.requests = requests

            dance_user.availability_set.order_by('day')
            
            try:
                serializer = DanceUserSerializer(dance_user, context={'request': request})
                return Response(serializer.data)

            except Request.DoesNotExist as ex:
                pass
        
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




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')



class DancePartnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'img', 'user')

class LeaderSerializer(serializers.ModelSerializer):
    follower = DancePartnerSerializer()

    class Meta:
        model = Partner()
        fields = ('id', 'follower')

class FollowerSerializer(serializers.ModelSerializer):
    leader = DancePartnerSerializer()

    class Meta:
        model = Partner()
        fields = ('id', 'leader')



class RequestUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'img', 'user')

class RequestSerializer(serializers.ModelSerializer):
    sender = RequestUserSerializer()
    # receiver = RequestUserSerializer()

    class Meta:
        model = Request
        fields = ('id', 'sender', 'receiver')


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ('id', 'day', 'start', 'end')
        depth = 1


class DanceUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    leader = LeaderSerializer(many=True)
    follower = FollowerSerializer(many=True)
    requests = RequestSerializer(many=True)
    availability_set = AvailabilitySerializer(many=True)


    class Meta:
        model = DanceUser
        fields = ('id', 'bio', 'img', 'user', 'leader', 'follower', 'requests', 'availability_set')
        depth = 2
