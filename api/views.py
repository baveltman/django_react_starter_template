from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]