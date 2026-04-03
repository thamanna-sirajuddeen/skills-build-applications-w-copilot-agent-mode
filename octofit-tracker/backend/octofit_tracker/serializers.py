# Serializers for Octofit Tracker API
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    team_id = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField()

class ActivitySerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    user_email = serializers.EmailField()
    activity = serializers.CharField()
    duration = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    suggested_for = serializers.CharField()

class LeaderboardSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    team = serializers.CharField()
    points = serializers.IntegerField()
