from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.AllowAny]

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def api_root(request, format=None):
    codespace_url = 'https://super-disco-7vgj7r67v79f7g5-8000.app.github.dev/'
    local_url = 'http://localhost:8000/'
    return Response({
        'users': codespace_url + 'api/users/?format=api',
        'teams': codespace_url + 'api/teams/?format=api',
        'activity': codespace_url + 'api/activity/?format=api',
        'workouts': codespace_url + 'api/workouts/?format=api',
        'leaderboard': codespace_url + 'api/leaderboard/?format=api',
        'users_local': local_url + 'api/users/?format=api',
        'teams_local': local_url + 'api/teams/?format=api',
        'activity_local': local_url + 'api/activity/?format=api',
        'workouts_local': local_url + 'api/workouts/?format=api',
        'leaderboard_local': local_url + 'api/leaderboard/?format=api',
    })
