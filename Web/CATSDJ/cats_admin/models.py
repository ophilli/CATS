import datetime
from django.db import models

class Certification(models.Model):
    name = models.CharField(max_length=30)
    # Expiration datetime
    # Prerequisite
    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    AGRICULTURE = 'AGR'
    ART = 'ART'
    BEHAVIOR = 'BEH'
    BUSINESS = 'BUS'
    EDUCATION = 'EDU'
    ENGINEERING = 'ENG'
    SCIENCE = 'SCI'

    COLLEGE_CHOICES = (
        (AGRICULTURE, 'Agriculture, Foresty, Life Sciences'),
        (ART, 'Architecture, Arts and Humanities'),
        (BEHAVIOR, 'Behavioral, Social and Health Sciences'),
        (BUSINESS, 'Business'),
        (EDUCATION, 'Education'),
        (ENGINEERING, 'Engineering, Computing and Applied Sciences'),
        (SCIENCE, 'Science'),
    )

    college = models.CharField(
        max_length = 3,
        choices = COLLEGE_CHOICES,
        default = ENGINEERING,
    )

    def __str__(self):
        return self.name

    def get_student_count(self):
        return -1 # the number of students in this major

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)  # Used for emails
    cuid = models.CharField(max_length=9, primary_key=True) # Shouldn't change - primary key? | Also good for looking up info
    rfid = models.CharField(max_length=11, unique=True)  # Necessary for RFID scanning
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    join_date = models.DateTimeField('Date Registered', auto_now_add=True) # Interesting user data?
    cert_group = models.ManyToManyField(Certification, blank=True, default=None)
    major = models.ForeignKey(Major, on_delete=models.PROTECT) # Users can have one major, majors can have many users

    FRESHMAN = 'FR'
    SOPHOMORE = 'S0'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    MASTERS = 'MA'
    PHD = 'Ph'
    FACULTY = 'FA'

    AFFLILIATION_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (MASTERS, 'Masters'),
        (PHD, 'PhD'),
        (FACULTY, 'Faculty'),
    )

    affiliation = models.CharField(
        max_length = 2,
        choices = AFFLILIATION_CHOICES,
        default = FRESHMAN,
    )

    def get_certs(self):
        return "\n|\n".join([c.name for c in self.cert_group.all()])

    def __str__(self):
        return self.first_name + " " + self.last_name

class Node(models.Model):
    id = models.CharField(max_length = 30, primary_key=True)
    name = models.CharField(max_length=30)
    certs = models.ManyToManyField(Certification)

    def __str__(self):
        return self.name

class Space(Node):
    staff = models.ManyToManyField(User)
    def get_machines(self):
        return -1 # the list of machines in this space

class Machine(Node):
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    serial = models.CharField(max_length=30)
    location = models.ForeignKey(Space, on_delete=models.PROTECT) # Protect the machines from being deleted if a space is deleted

    def get_certs(self):
        return "\n".join([c.cert_name for c in self.cert_group.all()])

class Event(models.Model):
    timestamp = models.DateTimeField('Time of Event', auto_now_add=True, primary_key=True)

    node = models.ForeignKey('Node', on_delete=models.PROTECT)
    user = models.ForeignKey('User', on_delete=models.PROTECT)

    SUCCESS = 'SE'
    NOT_AUTH = 'NA'
    MACH_ERR = 'ME'
    RFID_NOT_FOUND = 'RNF'
    MULTIPLE_LOGIN = 'ML'
    NODE_NOT_FOUND = 'HNF'

    STATUS_CHOICES = (
        (SUCCESS, 'Successful Entry'),
        (NOT_AUTH, 'Not Authorized'),
        (MACH_ERR, 'Machine Error'),
        (RFID_NOT_FOUND, 'Input Device Not Found'),
        (MULTIPLE_LOGIN, 'Multiple Login Attempt'),
        (NODE_NOT_FOUND, 'Node ID Not Recognized'),
    )

    status = models.CharField(
        max_length = 3,
        choices = STATUS_CHOICES,
        default = SUCCESS,
    )

    def __str__(self):
        return self.get_status_display() + " @ " + str(self.timestamp)
