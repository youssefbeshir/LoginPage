from django.db import models

# Create your models here.

class examcenter (models.Model):
    """ Exam center table in the database """
    ExamCenterID = models.CharField(max_length= 255,primary_key=True)
    governorate = models.CharField(max_length=255) 
    
    
class proctor(models.Model):
    """Proctor Table in the database """
    ID = models.CharField(max_length=255, primary_key=True, null=False)
    first_name = models.CharField(max_length=255, null = False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255)
    ExamCenterID = models.ForeignKey(examcenter, on_delete=models.CASCADE )
    dob = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    
    