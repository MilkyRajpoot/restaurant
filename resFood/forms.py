from django import forms  
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=255,required=True)

    class Meta:
        model = User
        fields = ('name', 'email','password1', 'password2')

    widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter School-Code','class':'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter User-Id','class':'form-control'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter School-Code','class':'form-control'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Enter School-Code','class':'form-control'}),
        }

# foodAttribute
# foodCategory
# foodItem
class foodForm(forms.ModelForm):

    class Meta:
        model = foodItem
        fields = ('item','price','category', 'attribute')

    widgets = {
            'item': forms.Select(attrs={'id':'choicewa'}),
            'attribute': forms.Select(attrs={'id':'choicewa'}),
            'category': forms.Select(attrs={'id':'choicewa'}),
            }

class foodattributeForm(forms.ModelForm):

    class Meta:
        model = foodAttribute
        fields = '__all__'

class foodCategoryForm(forms.ModelForm):

    class Meta:
        model = foodCategory
        fields = '__all__'
