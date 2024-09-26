from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    type = models.CharField(max_length=7, null=True, blank=True)
    credits = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class CurrentGPA(models.Model):
    current_weighted_gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    current_unweighted_gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    