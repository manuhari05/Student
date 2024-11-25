
# these are the django imports
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# these are the local imports 
from .utils import passing_marks , update_teacher_performance

# Create your models here.
class Teacher(models.Model):
    empid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    # subject=models.CharField(max_length=50)
    performance = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.name 
    

    
class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.AutoField(primary_key=True)
    # classteacher=models.CharField(max_length=50)
    teacher_id=models.ForeignKey('Teacher', on_delete=models.DO_NOTHING,null=True,blank=True)
    phy_marks=models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(50)])
    che_marks=models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(50)])
    maths_marks=models.FloatField(default=0,validators=[MinValueValidator(0),MaxValueValidator(50)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    total_marks=models.FloatField(editable=False)
    percentage=models.FloatField(editable=False)
    phy_pass=models.BooleanField(editable=False)
    che_pass=models.BooleanField(editable=False)
    maths_pass=models.BooleanField(editable=False)
    result=models.BooleanField(editable=False)



    def save(self, *args, **kwargs):

        



        self.total_marks=self.phy_marks+self.che_marks+self.maths_marks
        self.percentage=round((self.total_marks/150)*100,2)
        self.phy_pass=self.phy_marks>=passing_marks
        self.che_pass=self.che_marks>=passing_marks
        self.maths_pass=self.maths_marks>=passing_marks
        self.result=self.phy_pass and self.che_pass and self.maths_pass

        super(Student, self).save(*args, **kwargs)

        if self.teacher_id:
            update_teacher_performance(self.teacher_id)
        
    def delete(self, *args, **kwargs):
        teacher = self.teacher_id
        super(Student, self).delete(*args, **kwargs)
        if teacher:
            update_teacher_performance(teacher)

    def __str__(self):
       return self.name + " " + str(self.rollno)


