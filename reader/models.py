from enum import unique
from tabnanny import verbose
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
import re
from main.models import Faculty
# Create your models here.

def validate_passport(passport):
    if not re.match(r"[A-Z][A-Z]\d\d\d\d\d\d\d$",passport):
        raise ValueError("Passport raqami noto'g'ri")
    return passport


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE,verbose_name="Fakulteti")
    name = models.CharField(verbose_name="Ismi", max_length=20)
    surname = models.CharField(verbose_name="Familyasi", max_length=20)
    middlename = models.CharField(verbose_name="Otasini ismi", max_length=20)
    pinfl = models.CharField(verbose_name="PINFL raqami", max_length=14, unique=True)
    passport = models.CharField(verbose_name="passport raqami",
        max_length=9,unique=True,validators=[validate_passport])
    phone = models.CharField(verbose_name="Telefon raqami", max_length=13)
    email = models.EmailField(verbose_name="Email pochtasi", max_length=25)
    reg_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

        


