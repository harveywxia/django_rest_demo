from django.db import models


# Create your models here.

class Course(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='Cid')
    name = models.CharField(max_length=50)
    # pick_time = models.DateTimeField('date picked')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """一个课程-->多个老师"""
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    # 设置了related_name后才能在serialize中序列化course中的teachers列表
    course = models.ForeignKey(Course, related_name='teachers', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
