from django import forms # type: ignore
from .models import Student

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = Student
        fields="__all__"
        labels={
            "fname":"First Name",
            "lname":"Last Name",
            "email":"Email",
            "phone":"Phone Number",
            "branch":"Branch"
        }
        widgets={
            "fname":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "lname":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "email":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "phone":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "branch":forms.Select(attrs={"class":"form-control mb-3"}),
        }