from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from project_name.api.v1.auth.serializers import LoginSerializer


class LoginViewSet(viewsets.ViewSet):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(serializer.get_data(request), status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
