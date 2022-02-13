from django.contrib import admin
from .models import Upload, Testimonial, Contact, Profile, Subscriber

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Upload)
