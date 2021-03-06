from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

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
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self, request , pk=None):
        """Handles update scenario """
        return Response({'message':'PUT'})

    def patch(self, request , pk=None):
        """Handles partial update scenario"""
        return Response({'message':'PATCH'})

    def delete(self, request , pk=None):
        """deletes an object based on pk"""            
        return Response({'message':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a list of current viewset"""

        viewset_list = [
            'User\'s action (list,create,retrieve ,update , partial_update)',
            'Automatically maps to the urls using Routers.',
            'Provides more functionality with less code.',
        ]

        return Response({'message':'Hello From ViewSet' , 'viewset':viewset_list})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =  serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )            

    def retrieve(self, request, pk=None):
        """Handle Getting an object by Id"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating full object by its ID"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of object"""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing of an object"""

        return Response({'http_method':'DELETE'})






