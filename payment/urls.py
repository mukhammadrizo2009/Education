from django.urls import path
from .views import PaymentAPIView , GroupStudentsAPIView

urlpatterns = [
    path('payments/', PaymentAPIView.as_view()),
   path('groups/<int:group_id>/students/', GroupStudentsAPIView.as_view()),
]