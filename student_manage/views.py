from django.shortcuts import render # type: ignore
from .models import Student
from .forms import StudentInfoForm
from django.http import HttpResponseRedirect # type: ignore

# Create your views here.
def list_student(request):
    st = Student.objects.all().values()
    return render(request, "student_manage/list_student.html", {"st":st})
def update_student(request, id):
    if request.method == 'POST':
        st = Student.objects.get(pk=id)
        fm=StudentInfoForm(request.POST, instance=st)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        st = Student.objects.get(pk=id)
        fm=StudentInfoForm(instance=st)
    return render(request, "student_manage/update_student.html", {"form":fm})

def delete_student(request,id):
    if request.method == 'POST':
        st=Student.objects.get(pk=id)
        st.delete()
        return HttpResponseRedirect("/")
    
def add_student(request):
    if request.method == "POST":
        fm = StudentInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm = StudentInfoForm()
    return render(request, "student_manage/add_student.html", {"form":fm})