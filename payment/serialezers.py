from rest_framework import serializers
from student.models import Student

class PaymentSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)