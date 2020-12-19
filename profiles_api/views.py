from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """APi View to test Hello World"""

    serializer_class = serializers.HelloSerializer

    def get(self, request ,format=None):
        """Test an APIView"""
        an_apiview = [
            'Uses HTTP functions as method (get, post, put ,patch, delete)',
            'Is similar to a traditional Django view',
            'gives the most control over your application logic',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview })

    
    def post(self,request):
        """Creates a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response(serializer.errors,status = status .HTTP_400_BAD_REQUEST)

    def put(self, request , pk=None):
        """Handles update scenario """
        return Response({'message':'PUT'})

    def patch(self, request , pk=None):
        """Handles partial update scenario"""
        return Response({'message':'PATCH'})

    def delete(self, request , pk=None):
        """deletes an object based on pk"""            
        return Response({'message':'DELETE'})

