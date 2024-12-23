from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Hello, World!"}
        return Response(data)
