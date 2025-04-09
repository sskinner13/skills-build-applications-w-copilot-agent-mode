from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    email = serializers.EmailField()
    name = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()
    date = serializers.DateField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
