from base64 import b64encode

from rest_framework import serializers
from itsdangerous import TimedJSONWebSignatureSerializer

from django.conf import settings

from project_name.custom_profile import models


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, data):
        try:
            self.profile = models.Profile.objects.get(user__username=data.get('username'))
            if not self.profile.user.check_password(data.get('password')):
                raise serializers.ValidationError('Usuário ou senha não conferem.', code='invalid')
        except models.Profile.DoesNotExist:
            raise serializers.ValidationError('Usuário ou senha não conferem.', code='invalid')

        return data

    def get_token(self):
        serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=settings.EXPIRES_IN)
        token = serializer.dumps({'username': self.validated_data.get('username'),
                                  'password': self.validated_data.get('password')})
        return b64encode(token)

    def get_data(self, request):
        context = {'request': request}
        data = {
            'token': self.get_token(),
            'profile': ProfileSerializerRetrieve(
                models.Profile.objects.get(id=self.profile.pk), context=context).data
        }
        return data


class ProfileSerializerRetrieve(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = ['name', 'email']

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_email(self, obj):
        return obj.user.email
