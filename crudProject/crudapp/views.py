from django.shortcuts import render, HttpResponseRedirect
from crudapp.forms import StudentRegistrationForm
from .models import StudentRegistrationModel

# Create your views here.

# this function both adds data 
# and also shows all data on page
def adding(request):
    if request.method == 'POST':
        formObject = StudentRegistrationForm(request.POST)
        if formObject.is_valid():
            studentName = formObject.cleaned_data['name']
            studentEmail = formObject.cleaned_data['email']
            studentPassword = formObject.cleaned_data['password']
            model = StudentRegistrationModel(name=studentName, email=studentEmail, password = studentPassword)
            model.save()
            formObject = StudentRegistrationForm()
        else:
            print('Sorry not valid data')
    else:
        formObject = StudentRegistrationForm()
    students = StudentRegistrationModel.objects.all()
    return render(request, 'crudapp/adding.html', {'fmObject':formObject, 'students':students})


# this function is used to delete 
# the clicked data
def deleting(request, stdId):
    if request.method == 'POST':
        student = StudentRegistrationModel.objects.get(pk=stdId)
        student.delete()
        return HttpResponseRedirect('/')
    

# This function is used to 
# edit data of the Student
def editing(request,stdId):
    if request.method == 'POST':
        student = StudentRegistrationModel.objects.get(pk=stdId)
        formObject = StudentRegistrationForm(request.POST, instance=student)
        if formObject.is_valid():
            formObject.save();
    else:
        student = StudentRegistrationModel.objects.get(pk=stdId)
        formObject = StudentRegistrationForm(instance=student)
    return render(request, 'crudapp/updating.html', {'fmObject':formObject})