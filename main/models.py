from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Faculty(models.Model):
    title = models.CharField(verbose_name="Fakultet nomi", max_length=60)
    desc = models.TextField(verbose_name="Fakultet haqida", blank=True)
    image = models.ImageField(verbose_name="Fakultet rasmi", upload_to="faculty_photo", blank=True)
    

