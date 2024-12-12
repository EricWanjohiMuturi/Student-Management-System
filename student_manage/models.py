from django.db import models # type: ignore

CHOICES=[
    ("CE","CE"),
    ("EXTC","EXTC"),
    ("ME","ME"),
    ("AI","AI"),
    ("IT","IT")

]

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    branch=models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return f'{self.fname}'

