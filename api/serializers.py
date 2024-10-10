from rest_framework import serializers
from .models import Role, User, Service, Vehicle, Appointment, ServiceDetail
from django.contrib.auth.hashers import make_password

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'role_name', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}  # Пароль только для записи


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_id', 'service_name', 'description', 'price', 'duration_minutes']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_id', 'user', 'make', 'model', 'year']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_id', 'vehicle', 'service_date', 'status', 'total_cost', 'created_at', 'updated_at']


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = ['service_detail_id', 'appointment', 'service', 'quantity', 'cost']


# Сериализатор для регистрации
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}  # Пароль только для записи

    def create(self, validated_data):
        # Хеширование пароля перед сохранением (без соли, как указано)
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


# Сериализатор для авторизации
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()