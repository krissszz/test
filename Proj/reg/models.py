from django.db import models
import datetime
import os

# Create your models here.

class Applicant(models.Model):
    #personal_info
    studentId = models.CharField(max_length=20, null=True)
    studentStatus = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    suffix = models.CharField(max_length=8)
    gender = models.CharField(max_length=10)
    # age = models.CharField(max_length=3)
    birthofdate = models.CharField(max_length=45)
    birthofplace = models.CharField(max_length=45)
    religion = models.CharField(max_length=45)
    citizenship = models.CharField(max_length=45)
    contactno = models.CharField(max_length=20)
    DateRegistered = models.CharField(max_length=255)
    #residence
    presentAddress = models.CharField(max_length=50)
    homeAddress = models.CharField(max_length=50)
    #parents_info
    motherFirstname = models.CharField(max_length=20)
    motherMiddlename = models.CharField(max_length=20)
    motherLastname = models.CharField(max_length=20)
    motherOccupation = models.CharField(max_length=50)
    motherContact = models.CharField(max_length=20)
    fatherFirstname = models.CharField(max_length=20)
    fatherMiddlename = models.CharField(max_length=20)
    fatherLastname = models.CharField(max_length=20)
    fatherOccupation = models.CharField(max_length=50)
    fatherContactno = models.CharField(max_length=15)
    #guardians_info
    GuardianName = models.CharField(max_length=50)
    GuardianOccupation = models.CharField(max_length=50)
    GuardianAddress = models.CharField(max_length=50)
    GuardianContactno = models.CharField(max_length=20)
    #spouse_info
    SpouseName = models.CharField(max_length=50)
    SpouseOccupation = models.CharField(max_length=50)
    SpouseAddress = models.CharField(max_length=50)
    #previous_school_info
    JHSLastAttended = models.CharField(max_length=10)
    JHSdateLastAttended = models.DateField()
    SHSLastAttended = models.CharField(max_length=60)
    SHSDateLastAttended = models.DateField()
    CollegiateLastAttended = models.CharField(max_length=50)
    CollegiateDateLastAttended = models.DateField()
    #requirements
    Clearance = models.CharField(max_length=10)
    Sid = models.CharField(max_length=10)
    psa = models.CharField(max_length=10)
    Form148 = models.CharField(max_length=10)
    Form137 = models.CharField(max_length=10)
    GoodMoral = models.CharField(max_length=10)
    Credential = models.CharField(max_length=10)
    Picture = models.CharField(max_length=10)
    Envelop = models.CharField(max_length=10)
    #generated_refno
    refno = models.CharField(max_length=8)
    #status
    studentStatus = models.CharField(max_length=10)
    status = models.CharField(max_length=20, default='Pending')
    #temporary password - contactno
    password = models.CharField(max_length=15, default='')


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Item(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

