from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from project_name.api.auth.serializers import LoginSerializer


class LoginViewSet(viewsets.ViewSet):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response({'token': serializer.get_token()}, status=status.HTTP_200_OK)

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
