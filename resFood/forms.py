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
        fields = ('item', 'category', 'attribute')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = foodCategory.objects.none()
        self.fields['attribute'].queryset = foodAttribute.objects.none()

    widgets = {
            'item': forms.Select(attrs={'id':'choicewa'}),
            'attribute': forms.Select(attrs={'id':'choicewa'}),
            'category': forms.Select(attrs={'id':'choicewa'}),
            }