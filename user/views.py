from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User

from user.serializers import UserSerializer, LoginSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response( {"message":"User registered successfully"}, status=status.HTTP_201_CREATED)


def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(
        serializer.validated_data,
        status=status.HTTP_200_OK
    )

