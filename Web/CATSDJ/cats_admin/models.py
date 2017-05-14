import datetime

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    cuid = models.CharField(max_length=30)
    t1String = models.CharField(max_length=11)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_2fa = models.BooleanField()

    FRESHMAN = 'FR'
    SOPHOMORE = 'S0'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )

    year_in_school = models.CharField(
        max_length = 2,
        choices = YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

class Machine(models.Model):
    hostname = models.CharField(max_length=30)
    mach_type = models.CharField(max_length=30)
    mach_sn = models.CharField(max_length=30)
    mach_2fa = models.BooleanField()

    def __str__(self):
        return self.hostname + " " + self.mach_type

class Event(models.Model):
    mach_hostname = models.ForeignKey('Machine', on_delete=models.PROTECT)
    cuid = models.ForeignKey('User', on_delete=models.PROTECT)

    SUCCESS = 'SE'
    NOT_AUTH = 'NA'
    MACH_ERR = 'ME'
    RFID_NOT_FOUND = 'RNF'
    MULTIPLE_LOGIN = 'ML'
    HOST_NOT_FOUND = 'HNF'

    STATUS_CHOICES = (
        (SUCCESS, 'Successful Entry'),
        (NOT_AUTH, 'Not Authorized'),
        (MACH_ERR, 'Machine Error'),
        (RFID_NOT_FOUND, 'Input Device Not Found'),
        (MULTIPLE_LOGIN, 'Multiple Login Attempt'),
        (HOST_NOT_FOUND, 'Hostname Not Found'),
    )

    status = models.CharField(
        max_length = 3,
        choices = STATUS_CHOICES,
        default = SUCCESS,
    )

    timestamp = models.DateTimeField('Time of Event')

    def __str__(self):
        return self.get_status_display() + " @ " + str(self.timestamp)
