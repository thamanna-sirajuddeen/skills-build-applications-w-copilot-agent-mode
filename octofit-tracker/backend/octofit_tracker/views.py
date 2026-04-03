from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

client = MongoClient('localhost', 27017)
db = client['octofit_db']

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(db.users.find())
        for u in users:
            u['_id'] = str(u['_id'])
            u['team_id'] = str(u['team_id'])
        return Response(UserSerializer(users, many=True).data)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(db.teams.find())
        for t in teams:
            t['_id'] = str(t['_id'])
        return Response(TeamSerializer(teams, many=True).data)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(db.activities.find())
        for a in activities:
            a['_id'] = str(a['_id'])
        return Response(ActivitySerializer(activities, many=True).data)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(db.workouts.find())
        for w in workouts:
            w['_id'] = str(w['_id'])
        return Response(WorkoutSerializer(workouts, many=True).data)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = list(db.leaderboard.find())
        for l in leaderboard:
            l['_id'] = str(l['_id'])
        return Response(LeaderboardSerializer(leaderboard, many=True).data)
