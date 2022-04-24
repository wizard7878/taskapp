from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializer import SignUpSerializer
# Create your views here.


class SignUpViewSet(viewsets.ViewSet):

    serializer_class = SignUpSerializer
    def create(self, request, *args, **kwargs):
        signup_serializer = self.serializer_class(data=request.data)
        if signup_serializer.is_valid():
            user = User.objects.create(**signup_serializer.data)
            user.set_password(request.data.get('password'))
            user.save()
            return Response(signup_serializer.data)
        return Response(signup_serializer.errors, status= status.HTTP_400_BAD_REQUEST)