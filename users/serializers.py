from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# from django.core.mail import send_mail
from .models import User
import random, string

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'role', 'is_blocked', 'is_deleted']
        read_only_fields = ['id', 'username', 'role']

class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name','username', 'email', 'phone', 'password']

    def create(self, validated_data):
        return User.objects.create(
            name=validated_data.get('name'),
            username=validated_data['email'].split('@')[0],  # Auto username
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            role='customer',
            password=make_password(validated_data['password'])  # Hash password
        )

class DeliveryAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'phone', 'is_blocked', 'is_deleted']
        read_only_fields = ['id', 'username']

    def create(self, validated_data):
        email = validated_data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

        auto_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        agent = User.objects.create(
            name=validated_data.get('name'),
            username=email.split('@')[0],
            email=email,
            phone=validated_data.get('phone'),
            role='delivery_agent',
            password=make_password(auto_password)
        )

        # send_mail(
        #     'Your Delivery Agent Account',
        #     f'Hello {agent.name}, your account is created.\nUsername: {agent.username}\nPassword: {auto_password}',
        #     'admin@fooddelivery.com',
        #     [agent.email],
        #     fail_silently=False,
        # )

        return agent
