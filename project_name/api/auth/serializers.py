from base64 import b64encode

from itsdangerous import TimedJSONWebSignatureSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, data):
        try:
            user = User.objects.get(username=data.get('username'))
            if not user.check_password(data.get('password')):
                raise serializers.ValidationError('Usuário ou senha não conferem.', code='invalid')
        except User.DoesNotExist:
            raise serializers.ValidationError('Usuário ou senha não conferem.', code='invalid')

        return data

    def get_token(self):
        serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=settings.EXPIRES_IN)
        token = serializer.dumps({'username': self.validated_data['username'],
                                  'password': self.validated_data['password']})

        return b64encode(token)
