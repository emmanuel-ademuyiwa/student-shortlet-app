from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.
from django.shortcuts import reverse


type = [
    ['Flat', 'Flat'],
    ['Self contain', 'Self contain'],
    ['Single room', 'Single room'],
]

town = [
    ['Ago', 'Ago'],
    ['Igbo_Igbo', 'Ijebu Igbo'],
    ['Oru', 'Oru'],
]


IMAGES_CHOICES = {
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
}

default = 'pics'

"""class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    purpose = models.CharField(max_length=7)

    def __str__(self):
        return str(self.user)"""

class Profile(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+2349063435621'.")
    phone = models.CharField(validators=[phone_regex], max_length=14, null=True, blank=True)
    whatsApp = models.CharField(validators=[phone_regex], max_length=14, null=True, blank=True)
    purpose = models.CharField(max_length=7)
    REQUIRED_FIELDS = ['phone', 'name', 'purpose']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email




class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


class Upload(models.Model):
    hallname = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=3000)
    description = models.TextField(max_length=5000)
    type = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    price = models.PositiveIntegerField("Price")
    landlord = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=100)
    whatsApp = models.CharField(max_length=100)
    extra_facility = models.CharField(max_length=1000, blank=True)
    numbers = models.PositiveIntegerField(null=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    image1 = models.FileField(upload_to='pics/', null=True, blank=True)
    image2 = models.FileField(upload_to='pics/', null=True, blank=True)
    image3 = models.FileField(upload_to='pics/', null=True, blank=True)
    image4 = models.FileField(upload_to='pics/', null=True, blank=True)
    image5 = models.FileField(upload_to='pics/', null=True, blank=True)
    image6 = models.FileField(upload_to='pics/', null=True, blank=True)
    image7 = models.FileField(upload_to='pics/', null=True, blank=True)
    image8 = models.FileField(upload_to='pics/', null=True, blank=True)
    image9 = models.FileField(upload_to='pics/', null=True, blank=True)
    image10 = models.FileField(upload_to='pics/', null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.hallname)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.hallname)

    @property
    def image1URL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url

    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def image3URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def image4URL(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url

    @property
    def image5URL(self):
        try:
            url = self.image5.url
        except:
            url = ''
        return url

    @property
    def image6URL(self):
        try:
            url = self.image6.url
        except:
            url = ''
        return url

    @property
    def image7URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def image8URL(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url

    @property
    def image9URL(self):
        try:
            url = self.image5.url
        except:
            url = ''
        return url

    @property
    def image10URL(self):
        try:
            url = self.image6.url
        except:
            url = ''
        return url
