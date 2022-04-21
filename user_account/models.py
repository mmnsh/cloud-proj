from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from doctors_office_management_system import settings

class all_users(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    password = models.CharField(max_length=32, null=False, blank=False)
    role = models.IntegerField(null=False, blank=False)

class normal_user(models.Model):
    user_id = models.ForeignKey(all_users, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=300,null=False, blank=False)

class doctor(models.Model):
    user_id = models.ForeignKey(all_users, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False)
    address = models.CharField(max_length=500,null=False, blank=False)
    education = models.CharField(max_length=300,null=False, blank=False)
    field = models.CharField(max_length=300,null=False, blank=False)
    dNumber = models.IntegerField(null=False, blank=False, unique = True)

class comment(models.Model):
    user_id = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

class appointment(models.Model):
    user_id = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)

class working_time(models.Model):
    class Day(models.TextChoices):
        SATURDAY = 'Sat.', _('Saturday')
        SUNDAY = 'Sun.', _('Sunday')
        MONDAY = 'Mon.', _('Monday')
        TUESDAY = 'Tue.', _('Tuesday')
        WEDNESDAY = 'Wed.', _('Wednesday')
        THURSDAY = 'Thu.', _('Thursday')
        FRIDAY = 'Fri.', _('Friday')

    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=4, choices=Day.choices, blank=False, null=False)
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)

class favorite(models.Model):
    user_id = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_id', 'doctor_id']
