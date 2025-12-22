from django.db import models
from student.models import Student
from teacher.models import Teacher

class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="groups")
    teacher = models.ManyToManyField(Teacher, related_name="groups")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"