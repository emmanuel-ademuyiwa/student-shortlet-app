from django import forms
from .models import Upload, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


type = [
    ['Flat', 'Flat'],
    ['Self contain', 'Self contain'],
    ['Single room', 'Single room'],
]

town = [
    ['ago-iwoye', 'Ago'],
    ['ijebu-igbo', 'Ijebu Igbo'],
    ['oru', 'Oru'],
]

purp = [
    ['Rent', 'Rent'],
    ['Sale', 'Sale'],
]

availability = [
    ['Available', 'Available'],
    ['Not Available', 'Not Available'],
]

purpose = [
    ['Student', 'Student'],
    ['Agent', 'Agent'],
]

IMAGES_CHOICES = {

    ('4', '4'),
    ('7', '7'),
    ('5', '5'),
    ('6', '6'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
}

class CreateUserForm(UserCreationForm):
    purpose = forms.CharField(label='Town', widget=forms.Select(choices=purpose))

    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'purpose', 'password1', 'password2']



class DocumentForm(forms.ModelForm):
    town = forms.CharField(label='Town', widget=forms.Select(choices=town))
    type = forms.CharField(label='Type', widget=forms.Select(choices=type))
    availability = forms.CharField(label='Availability', widget=forms.Select(choices=availability))
    description = forms.TextInput()
    landlord = forms.CharField(widget=forms.HiddenInput())
    numbers = forms.IntegerField(label="Numbers of images to be uploaded", widget=forms.Select(choices=IMAGES_CHOICES))
    image1 = forms.ImageField(label="1")
    image2 = forms.ImageField(label="2")
    image3 = forms.ImageField(label="3")
    image4 = forms.ImageField(label="4")
    image5 = forms.ImageField(label="5", required=False)
    image6 = forms.ImageField(label="6", required=False)
    image7 = forms.ImageField(label="7", required=False)
    image8 = forms.ImageField(label="8", required=False)
    image9 = forms.ImageField(label="9", required=False)
    image10 = forms.ImageField(label="10", required=False)


    class Meta:
        model = Upload
        fields = ('hallname', 'description', 'type',
                  'town', 'availability', 'price', 'landlord', 
                  'phone', 'numbers', 'image1', 'image2', 'image3', 
                  'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10', )
