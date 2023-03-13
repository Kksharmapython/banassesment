import random

from django.shortcuts import render
from mainapp.models import School, Student
import datetime
from rest_framework.views import APIView
from mainapp.serializers import StudentSerializer, SchoolStudentsSerial


# Create your views here.


def start_app(request):
    return render(request, "start_app.html")


def school_view(request):
    if request.method == "POST":
        school = School.objects.create(
            name=request.POST.get("name")
        )

        return render(request, "school.html", {"school": School.objects.all()})

    return render(request, "school.html")


def student_view(request):
    if request.method == "POST":
        school = Student.objects.create(
            name=request.POST.get("name"),
            school=School.objects.get(id=request.POST.get("school_id")),
            enrollment_number=f"{random.randint(111111, 999999)}{datetime.datetime.now()}"
        )

        return render(request, "student.html", {"school": School.objects.all(), "students": Student.objects.all()})

    return render(request, "student.html", {"school": School.objects.all(), "students": Student.objects.all()})


def delete_student(request, id):
    Student.objects.filter(id=id).delete()
    return render(request, "student.html", {"school": School.objects.all(), "students": Student.objects.all()})


from rest_framework.response import Response


class StudentDetail(APIView):
    """
    This api view is used to fetch detail of stundent
    """

    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
            return Response({
                'status': True,
                "message": "Student does not exist on given id",
                "data": {
                    "name": student.name,
                    "enrollment_number": student.enrollment_number,
                    "school": student.school.name}

            })
        except Student.DoesNotExist:
            return Response(
                {
                    'status': False,
                    "message": "Student does not exist on given id",

                }
            )


class SchoolDetail(APIView):
    """
    This api view is used to fetch detail of stundent
    """

    def get(self, request, school_id):
        try:
            school = School.objects.get(id=school_id)

            return Response({
                'status': False,
                "message": "Student does not exist on given id",
                "data": {
                    "name": school.name,
                    "id": school.id
                }})
        except School.DoesNotExist:
            return Response(
                {
                    'status': False,
                    "message": "School does not exist on given id",

                }
            )


class SchoolStudents(APIView):
    """
        This api view is used to fetch detail of stundent
        """

    def get(self, request):
        try:
            return Response({
                'status': True,
                "message": "Student does not exist on given id",
                "data": SchoolStudentsSerial(School.objects.all(), many=True).data})
        except School.DoesNotExist:
            return Response(
                {
                    'status': False,
                    "message": "School does not exist on given id",

                }
            )
