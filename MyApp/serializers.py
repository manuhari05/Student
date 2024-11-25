# these are rest_framework imports
from rest_framework import serializers

# these are local imports 
from .models import Student , Teacher

'''
This is a serializer class for the Teacher and it specifies the fields to be included in the serializer

'''

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'


'''
This is a serializer class for the Student and it specifies the fields to be included in the serializer

'''

class StudentSerializers(serializers.ModelSerializer):
    # teacher_id=TeacherSerializers()
    class Meta:
        model=Student
        fields='__all__'