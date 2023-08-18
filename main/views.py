import re
from django.shortcuts import render,HttpResponse,redirect
from .models import Professor,Student
from .forms import ProductForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('Student','ErrorDemo')
        cat = Student.objects.create(name=name)
    student_data = Student.objects.all()
    professor = Professor.objects.all()
    return render(request,'home.html',context={"professor":professor,"student_data":student_data})

def about(request):
    if request.method == 'POST':
        professor_form = ProductForm(request.POST)
        print(professor_form.is_valid())
        if professor_form.is_valid():
            professor_form.save()
    professor_form = ProductForm()
    professor = Professor.objects.all()
    print(professor)

    return render(request,'about.html',context={"professor_form":professor_form,"professor":professor})
            



def delete_professor(request,id):
    professor = Professor.objects.get(id=id)
    professor.delete()
    return redirect('about')

  



def update_professor(request,id):
    instance = Professor.objects.get(id=id)
    if request.method == 'POST':
        professor_form = ProductForm(request.POST,instance=instance)
        if professor_form.is_valid():
            professor_form.save()
            return redirect("about")
    professor_form = ProductForm(instance=instance)
    professor = Professor.objects.all()
    return render(request,'update_professor.html',context={"professor_form":professor_form,"professor":professor})
            

    
    



