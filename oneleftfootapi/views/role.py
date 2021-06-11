from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from oneleftfootapi.models import Role
from django.core.exceptions import ValidationError


class RoleView(ViewSet):

    
    def list(self, request):

        roles = Role.objects.all()

        serializer = RoleSerializer(
            roles, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        try:
            role = Role.objects.get(pk=pk)
            
            serializer = RoleSerializer(role, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)




class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'label')