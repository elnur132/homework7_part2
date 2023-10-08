from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def person_id(self):
        return str(self.id) + " " + self.name + " " + str(self.age)

    def __str__(self):
        return self.name