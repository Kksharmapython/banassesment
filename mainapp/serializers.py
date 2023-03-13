from rest_framework import serializers
from mainapp.models import School, Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    enrollment_number = serializers.CharField()

    class Meta:
        model = Student
        fields = ["name", "enrollment_number"]


class SchoolStudentsSerial(serializers.Serializer):
    name = serializers.CharField()
    students = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ["name", "students"]

    def get_students(self, obj):
        return StudentSerializer(Student.objects.filter(school__id=obj.id), many=True).data
