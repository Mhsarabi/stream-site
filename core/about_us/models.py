from django.db import models
from django.core.validators import RegexValidator

phone_validator=RegexValidator(
    regex=r'^\+?\d{10,15}$',
     message="شماره تلفن باید فقط شامل عدد باشد و بین 10 تا 15 رقم داشته باشد."
)
# Create your models here.
class ContactMessage(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
class Question(models.Model):
    question=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.question}-{self.answer[:10]}"

