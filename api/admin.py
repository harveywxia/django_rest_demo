from django.contrib import admin

# Register your models here.
from api.models import Student, Course, Teacher

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
