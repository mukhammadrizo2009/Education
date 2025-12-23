import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(
        field_name="full_name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Student
        fields = ["full_name"]