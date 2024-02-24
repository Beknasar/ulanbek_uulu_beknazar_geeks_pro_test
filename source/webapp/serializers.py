from django.contrib.auth import get_user_model
from rest_framework import serializers
from webapp.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
