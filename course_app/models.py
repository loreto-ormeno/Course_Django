from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def field_validator(self, postData):

        errors = {}

        if len(postData['name'].strip()) < 5:
                errors['name'] = "Nombre del curso debe tener al menos 5 caracteres"

        if len(postData['desc'].strip()) < 15:
                errors['desc'] = "La descripción debe tener al menos 15 caracteres"

        return errors


class Course (models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = CourseManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
