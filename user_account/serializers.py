from rest_framework import serializers
from .models import *


class allUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_users
        fields = '__all__'


class normalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = normal_user
        fields = '__all__'


class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = '__all__'


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'


class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'


class workingTimeSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%H:%M:%S")
    end_time = serializers.DateTimeField(format="%H:%M:%S")

    class Meta:
        model = working_time
        fields = '__all__'


class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorite
        fields = '__all__'
