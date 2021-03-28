from rest_framework import serializers
from myapp.models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['rollno','name','city']
