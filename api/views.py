
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Student, Course, Teacher
from api.serializers import StudentSerializer, CourseSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    this class is used for student view, it has default list,get, update and delete method
    ...

    Attributes
    ----------

    Methods
    -------
    age(self, request, *args, **kwargs)
        return student's age
    """

    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    # http://127.0.0.1:8000/students/2/age/
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def age(self, request, *args, **kwargs):
        student = self.get_object()
        return Response(student.age)

    # http://127.0.0.1:8000/students/?keyword=jim&sex=female
    def list(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        sex = request.GET.get('sex')
        # if keyword is not None:
        if keyword in ('', None) and sex not in ('', None):
            queryset = Student.objects.filter(sex=sex)
        elif keyword not in ('', None) and sex in ('', None):
            queryset = Student.objects.filter(name__contains=keyword)
        elif keyword not in ('', None) and sex not in ('', None):
            # 执行filter() 方法
            queryset = Student.objects.filter(name__contains=keyword, sex=sex)
        else:
            # 如果参数为空， 执行all()方法
            queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    """
    the course view sets
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    the teacher view sets
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
