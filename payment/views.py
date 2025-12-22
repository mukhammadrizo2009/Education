from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from groups.models import Group
from student.models import Student
from .models import Payment
from .serialezers import PaymentSerializer
from student.serialezers import StudentSerializer

class GroupStudentsAPIView(APIView):
    def get(self, request, group_id):
        group = Group.objects.get(id=group_id)
        students = group.students.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class PaymentAPIView(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_id = serializer.validated_data['student_id']
        amount = serializer.validated_data['amount']

        student = Student.objects.select_for_update().get(id=student_id)

        # balansga qo‘shish
        student.balance += amount
        student.save()

        # payment history
        Payment.objects.create(
            student=student,
            amount=amount
        )

        return Response({
            "message": "To‘lov muvaffaqiyatli amalga oshirildi",
            "new_balance": student.balance
        }, status=status.HTTP_200_OK)