from django import forms
from micropro.models import Userprofileinfo
from django.contrib.auth.models import User



class Userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password')




class Userprofileinfoform(forms.ModelForm):


    class Meta:
        model = Userprofileinfo
        fields = ('portfolio','profilepic')

'''
class Testingform(forms.ModelForm):
    firstname = forms.CharField(required =True)
    lastname = forms.CharField(required = True)
    email = forms.EmailField(required = True,widget = forms.EmailInput)
    username = forms.CharField(required = True)
    password = forms.CharField(widget = forms.PasswordInput)
    choice = [(1,'Male'),(2,'Female')]
    Choices = forms.ChoiceField(widget = forms.RadioSelect, choices =choice)
    feedback = forms.CharField(widget = forms.Textarea)
    selection = [(1,'Mango'),(2,'Apple'),(3,'banana')]
    selective =forms.ChoiceField(widget = forms.Select,choices = selection)
    multiselection = forms.ChoiceField(widget = forms.SelectMultiple,choices = selection)
    multiselectcheckbox = forms.ChoiceField(widget = forms.CheckboxSelectMultiple,choices=selection)

    class Meta:
        model =
        fields = '__all__'
'''
