from django.db import models

# Create your models here.

#------------------------------- Location -------------------------------------#
class Region(models.Model):
 
    region_name =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Region')

    #def get_absolute_url(self):
        #return reverse('expenses:expense-payables-details', args=[self.slug])

    def __str__(self):
        return self.region_name

    class Meta():
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        #ordering: ['-created_at']

class Country(models.Model):
 
    country_name =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Country')
    region =  models.ForeignKey(Region, on_delete=models.SET_NULL,  null = True, blank = True, verbose_name = 'Region')

    #def get_absolute_url(self):
        #return reverse('expenses:expense-payables-details', args=[self.slug])

    def __str__(self):
        return self.country_name

    class Meta():
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        #ordering: ['-created_at']


class Cities(models.Model):
    city_name =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'City')
    country =  models.ForeignKey(Country, on_delete=models.SET_NULL,  null = True, blank = True, verbose_name = 'Country')
    latitude =  models.FloatField(null=True, default=0, blank = True, verbose_name = 'Latitude')
    longitude =  models.FloatField(null=True, default=0, blank = True, verbose_name = 'Longitude')

    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)


    #def get_absolute_url(self):
        #return reverse('expenses:expense-payables-details', args=[self.slug])

    def __str__(self):
        return self.city_name

    class Meta():
        verbose_name = 'Cities'
        verbose_name_plural = 'Cities'
        #ordering: ['-created_at']

#------------------------------- WORK LOCATION -------------------------------------#
class BranchManager(models.Model):
    manager_name = models.CharField(max_length=100, verbose_name="Branch Manager Name")    
    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return self.manager_name


    class Meta:
        verbose_name = ('Branch Manager')
        verbose_name_plural = ('Branch Managers')
        ordering = ['manager_name']

class WorkLocation(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Non-Active', 'Non-Active'),
    )

    location_name = models.CharField(max_length=100, default="", verbose_name="Work Location")
    address = models.CharField(max_length=100, default="", verbose_name="Work Address")
    branch_manager = models.ForeignKey(BranchManager, on_delete=models.SET_NULL,  null = True, blank = True, verbose_name = 'Branch Manager')    
    city =  models.ForeignKey(Cities, on_delete=models.SET_NULL, default="",  null = True, blank = True, verbose_name = 'City')
    status =  models.CharField(('Status'),max_length=255,blank=False, choices=STATUS, default='Active' )
    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return self.location_name


    class Meta:
        verbose_name = ('Work Location')
        verbose_name_plural = ('Work Locations')
        ordering = ['location_name']

#------------------------------- Branch MANAGER-------------------------------------#
class DepartmentManager(models.Model):
    manager_name = models.CharField(max_length=100, verbose_name="Branch Manager Name") 
    work_location = models.ForeignKey(WorkLocation, on_delete=models.SET_NULL,  null = True, blank = True, verbose_name = 'Location')    
    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return self.manager_name


    class Meta:
        verbose_name = ('Department Manager')
        verbose_name_plural = ('Department Managers')
        ordering = ['manager_name']

#------------------------------- Department / Role / -------------------------------------#
class Department(models.Model):
    #parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    name = models.CharField(max_length=125)
    manager_name = models.ForeignKey(DepartmentManager, blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Department')
        verbose_name_plural = ('Department')
        ordering = ['name']


class SubDepartment(models.Model):
    department = models.ForeignKey(Department, blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    name = models.CharField(max_length=125)

    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Sub Department')
        verbose_name_plural = ('Sub Department')
        ordering = ['name']




#------------------------------- JOB POSITION -------------------------------------#
class JobPosition(models.Model):
    sub_department = models.ForeignKey(SubDepartment, blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    job_position_name = models.CharField(max_length=125, verbose_name='Job Position')
    

    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)


    def __str__(self):
        return self.job_position_name

    class Meta:
        verbose_name = ('Job Position')
        verbose_name_plural = ('Job Positions')
        ordering = ['job_position_name']
