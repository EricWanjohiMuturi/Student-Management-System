from django.shortcuts import render # type: ignore
from .models import Student

# Create your views here.
def list_student(request):
    st = Student.objects.all().values()
    return render(request, "student_manage/list_student.html", {"st":st})
