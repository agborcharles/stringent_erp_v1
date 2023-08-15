from django.db import models
from configs_settings.models import *
from django.template.defaultfilters import slugify

# Create your models here.

class Employee(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    LEVELOFEDUCATION = (
        ('FSLC', 'FSLC'),
        ('Ordinary Level', 'Ordinary Level'),
        ('Advanced Level', 'Advanced Level'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Master Degree', 'Master Degree'),
        ('MBA', 'MBA'),
        ('PHD', 'PHD'),
    )

    RELIGION =  (
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Others', 'Others'),
    )

    EMERGENCYRELATIONSHIP =  (
        ('FATHER', 'FATHER'),
        ('MOTHER', 'MOTHER'),
        ('UNCLE', 'UNCLE'),
        ('AUNTY', 'AUNTY'),
        ('BROTHER', 'BROTHER'),
        ('SISTER', 'SISTER'),
        ('HUSBAND', 'HUSBAND'),
        ('WIFE', 'WIFE'),
        ('BOY FRIEND', 'BOY FRIEND'),
        ('GIRL FRIEND', 'GIRL FRIEND'),
        ('OTHERS', 'OTHERS'),
    )

    EMPLOYMENT_STATUS =  (
        ('ACTIVE', 'ACTIVE'),
        ('ON LEAVE', 'ON LEAVE'),
        ('SUSPENDED', 'SUSPENDED'),
        ('DIMISSED', 'DIMISSED'),
    )

    EMPLOYMENT_TYPE =  (
        ('PART TIME', 'PART TIME'),
        ('FULL TIME', 'FULL TIME'),
        ('CONTRACT', 'CONTRACT'),
    )

    # PERSONAL DATA
    employee_name = models.CharField(('Employees Name'),max_length=1250,null=False,blank=False, default="")
    #id_card_number = models.CharField(('ID Card Number'),max_length=30,null=True,blank=True)
    #profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    #slug = models.SlugField(max_length=1000, unique=True, blank=True, null=True)

    # Demographics
    #gender = models.CharField(('Gender'),max_length=255,blank=False, choices=GENDER,default='')
    #birthday = models.DateField(('Date of Birth (YY/MM/DD)'),blank=False,null=False, auto_now_add=True,)
    #birth_place = models.CharField(('Place of Birth (optional)'), max_length=255,blank=True,null=True)
    #tribe = models.CharField(('Tribe (optional)'), max_length=255,blank=True,null=True)
    #religion = models.CharField(('Religion (optional)'), max_length=255,default=None,blank=True,null=True, choices=RELIGION)
    #nationality = models.CharField(('Nationality (optional)'), max_length=255,default=None,blank=True,null=True)
    #ssnitnumber = models.CharField(('Social Insurance Number'),max_length=30,null=True,blank=True)

    manager = models.ForeignKey(BranchManager, on_delete=models.SET_NULL,  null = True, blank = True, verbose_name = 'Manager')
    role = models.ForeignKey(JobPosition, on_delete=models.SET_NULL,  null = True, blank = True, verbose_name = 'Role')


    class Meta:
        verbose_name = ('Employee')
        verbose_name_plural = ('Employees')
    #ordering = ['-created']

    def __str__(self):
        return self.employee_name
    
    