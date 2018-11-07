# -*- coding:utf-8 -*-
# --author:'xiawei'
# --date: '2018/11/2'
from rest_framework import serializers

from api.models import Student, Course, Teacher


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    """
    老师详情序列化
    """
    class Meta:
        model = Teacher
        fields = ("id", "name", "age")


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """
    课程详情序列化
    """
    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "name", "teachers")


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    """
    学生详情序列化
    """
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ("id", "name", "age", "sex", "courses")
