from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'profinity'
    id = models.AutoField(primary_key=True)
    username = models.CharField( unique=True)
    email = models.EmailField( unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    


class Employee(User):
    class Meta:
        app_label = 'profinity'
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resume/')
    image = models.ImageField(upload_to='profile_image/', blank=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    experience = models.IntegerField()
    salary = models.FloatField()
    propoints = models.IntegerField()
    Employment_Status = models.CharField(max_length=50)
    Work_Schedule = models.CharField(max_length=50)
    Skills_and_Qualifications = models.CharField(max_length=50)
    Performance_Ratings = models.FloatField()
    ROI = models.FloatField()
    milestones_passed = models.ManyToManyField('Milestone', blank=True)
    assigned_tasks = models.ManyToManyField('task', blank=True)
    

    def __str__(self):
        return self.name
    
    
class Milestone(models.Model):
    class Meta:
        app_label = 'profinity'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Department(models.Model):
    class Meta:
        app_label = 'profinity'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    number_of_employees = models.IntegerField()
    number_of_projects = models.IntegerField()
    projects = models.CharField(max_length=50)
    number_of_completed_projects = models.IntegerField()


    def __str__(self):
        return self.name
    

class Project(models.Model):
    class Meta:
        app_label = 'profinity'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.FloatField()
    status = models.CharField(max_length=50)
    number_of_employees = models.IntegerField()
    number_of_tasks = models.IntegerField()
    number_of_completed_tasks = models.IntegerField()
    milestones = models.ManyToManyField('Milestone', blank=True)
    # employees = models.ManyToManyField('emloyee', blank=True, related_name='employees')
    tasks = models.ManyToManyField('task', blank=True)
    documents = models.ForeignKey('document', blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Task(models.Model):
        class Meta:
            app_label = 'profinity'
        name = models.CharField(max_length=50)
        description = models.CharField(max_length=50)
        start_date = models.DateField()
        end_date = models.DateField()
        budget = models.FloatField()
        status = models.CharField(max_length=50)
        def __str__(self):
            return self.name
        
class Document(models.Model):
    class Meta:
        app_label = 'profinity'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.name
    
class company(models.Model):
    class Meta:
        app_label = 'profinity'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_logo/', blank=True)
    number_of_employees = models.IntegerField()
    Employees= models.ForeignKey('Employee', blank=True, on_delete=models.CASCADE)
    projects = models.ForeignKey('Project', blank=True, on_delete=models.CASCADE)
    departments = models.ForeignKey('Department', blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

