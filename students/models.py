from django.conf import settings
from django.db import models
from django.utils import timezone


class StudentGeneralInfo(models.Model):
    sid = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    sex = models.BooleanField(default=False)
    birth_date = models.DateField()
    ncode = models.IntegerField()
    ccode = models.IntegerField()
    army_service = models.BooleanField(default=False)
    army_standing = models.IntegerField()
    rtoefl = models.IntegerField()
    student_status_choices = [
        ('Active', 'Active'),
        ('Dismissed', 'Dismissed'),
        ('Academic leave', 'Academic leave'),
        ('Graduate', 'Graduate'),
    ]
    student_program_choices = [
        ('IT', 'IT'),
        ('BA', 'BA'),
        ('LAW', 'LAW'),
        ('IR', 'IR'),
        ('PED', 'PED'),
        ('LNG', 'LNG'),
        ('CHN', 'CHN'),
    ]

    def __unicode__(self):
        return self.last_name

class StudentGroup(models.Model):
    sid = models.ForeignKey(StudentGeneralInfo,on_delete=models.CASCADE)
    'cmajor = models.ForeignKey(MajorGeneralInfo,on_delete=models.CASCADE)'
    studgroup = models.CharField(max_length=3)
    yeargroup = models.IntegerField()
    incommingyear = models.IntegerField()
    semestr = models.IntegerField()


class MajorGeneralInfo(models.Model):
    majorid = models.AutoField(primary_key=True)
    majorrus = models.CharField(max_length=50)
    majoreng = models.CharField(max_length=50)
    majorkyr = models.CharField(max_length=50)
    licence = models.CharField(max_length=20)
    year_of_educ = models.IntegerField(default=4)

class ContactInfo(models.Model):
    sid = models.ForeignKey(StudentGeneralInfo,on_delete=models.CASCADE)
    pstreet = models.CharField(max_length=70)
    pcity = models.CharField(max_length=50)
    pstreetrus = models.CharField(max_length=70)
    pcityrus = models.CharField(max_length=50)
    pccode = models.IntegerField()
    pzip = models.CharField(max_length=6)
    pph = models.CharField(max_length=20)
    cstreet = models.CharField(max_length=70)
    ccity = models.CharField(max_length=50)
    cstreetrus = models.CharField(max_length=70)
    ccityrus = models.CharField(max_length=50)
    cccode = models.IntegerField()
    czip = models.CharField(max_length=6)
    cph = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=50)
    contact_ph = models.CharField(max_length=20)
    relation = models.CharField(max_length=20)

