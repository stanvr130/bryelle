from rest_framework import views, status, generics
from user.serializer import UserHomeSerializer, UserSchoolSerializer, UserVlogSerializers
from rest_framework.response import Response

class UserHomeView(generics.GenericAPIView):
    serializer_class = UserHomeSerializer
    def get(self, request):
        text = {"message": "Welcome Home"}
        return Response (data = text, status=status.HTTP_200_OK)
    def post(self, request):
        return Response(data={"message":"data received"}, status=201)
    def delete(self, request):
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class UserSchoolView(generics.GenericAPIView):
    serializer_class = UserSchoolSerializer
    def post(self, request):
        return Response(data = {"message":"done"}, status=201)
    
    
class UserVlogView(generics.GenericAPIView):
    serializer_class = UserVlogSerializers
    def post(self, request):
        return Response(data= {"message":"accepted"}, status=201)
    def delete(self, request):
        return Response(status= status.HTTP_204_NO_CONTENT)


    

# Create your views here.
