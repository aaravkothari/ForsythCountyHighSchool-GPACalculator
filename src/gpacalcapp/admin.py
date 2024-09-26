from django.contrib import admin
from .models import Course, CurrentGPA

# Register your models here.
admin.site.register(Course)
admin.site.register(CurrentGPA)