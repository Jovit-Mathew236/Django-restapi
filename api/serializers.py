from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class UserSignUp(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def save(self):
        reg = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']

        reg.set_password(password)
        reg.save()
        return reg


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
