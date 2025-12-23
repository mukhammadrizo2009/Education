from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView , StudentViewSet

urlpatterns = [
    path('students/', StudentViewSet.as_view({'get': 'list' , 'post': 'create'})),
    path('students/<int:pk>', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]