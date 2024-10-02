from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('admin', 'Admin'), ('user', 'User')])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'role']

    def validate_username(self, value):
        if CustomUser.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def create(self, validated_data):
        role = validated_data.pop('role')
        validated_data['username'] = validated_data['username'].lower()
        user = CustomUser.objects.create(**validated_data, is_admin=(role == 'admin'), )
        user.set_password(validated_data['password'])
        user.save()
        return user
