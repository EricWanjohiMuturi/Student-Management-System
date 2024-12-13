from django.shortcuts import render # type: ignore
from .models import Student
from .forms import StudentInfoForm

# Create your views here.
def list_student(request):
    st = Student.objects.all().values()
    return render(request, "student_manage/list_student.html", {"st":st})
def update_student(request, id):
    st = Student.objects.get(pk=id)
    fm=StudentInfoForm(instance=st)
    return render(request, "student_manage/update_student.html", {"form":fm})
