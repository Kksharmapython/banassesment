from django.urls import path
from mainapp import views

urlpatterns = [
    path("", views.start_app, name="start_app"),
    path("school_view/", views.school_view, name="school_view"),
    path("student_view/", views.student_view, name="student_view"),
    path("delete_student/<int:id>", views.delete_student, name="delete_student"),
    path("student/<int:student_id>/", views.StudentDetail.as_view(), name="student_detail"),
    path("school/<int:school_id>/", views.SchoolDetail.as_view(), name="school_view"),
    path("school/<int:school_id>/", views.SchoolDetail.as_view(), name="school_view"),
    path("schoolsStundets/", views.SchoolStudents.as_view(), name="school_student"),

]
