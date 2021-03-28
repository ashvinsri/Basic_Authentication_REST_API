from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Student
from myapp.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


# Create your views here.
