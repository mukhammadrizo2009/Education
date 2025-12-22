from django.db import models

class Student(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_rick = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        'groups.Group',
        related_name='groups',
        default="English 12:00 - 14:00",
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    