from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer
from rest_framework import response,status

# Create your views here.
class RegisterApiView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return response.Response(data=serializers.data,status=status.HTTP_201_CREATED)
                    
        return response.Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)

