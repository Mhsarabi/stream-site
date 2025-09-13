from django.contrib import admin
from .models import ContactMessage,Question

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Question)
