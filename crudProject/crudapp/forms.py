
from django import forms
from crudapp.models import StudentRegistrationModel


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistrationModel
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
    