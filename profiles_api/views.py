from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """APi View to test Hello World"""

    def get(self, request ,format=None):
        """Test an APIView"""
        an_apiview = [
            'Uses HTTP functions as method (get, post, put ,patch, delete)',
            'Is similar to a traditional Django view',
            'gives the most control over your application logic',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview })



