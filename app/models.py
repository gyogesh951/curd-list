from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
     
    def __str__(self):
            return self.name

class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    school=models.ForeignKey(school,on_delete=models.CASCADE,related_name='student')

    def __str__(self):
         return self.name

