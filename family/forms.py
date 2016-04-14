from django import forms
from models import UserInfo

ACCOUNT_CHOICES = (
    ('family', 'Family'),
    ('university', 'University'),
    ('school', 'School'),
)

BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+','AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),


)
class familyform(forms.Form):
    #class Meta:
    #    model = FamilyInfo

    #    fields = ['name','phone_no','age','image']
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)

    dateofbirth = forms.CharField(max_length=100, required=True,label="Date of Birth")
    Address = forms.CharField(max_length=100, required=False)
    bloodgroup = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES,required=True)
    image = forms.ImageField(required=False)


class UserSignUpform(forms.Form):
    username = forms.CharField(label= "username",required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,required=True)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput,required=True)

class loginform(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)


