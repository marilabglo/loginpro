from django.db import models







class students(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30,null = True)
    img=models.ImageField(upload_to="images/")
    
def __str__(self):
    return self.id, self.first_name,self.last_name,self.img
    
class marksheet(models.Model):
    student=models.ForeignKey(students,on_delete=models.CASCADE,null=True)
    sub = models.CharField(max_length=30,null = True)
    mark = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    created_by = models.CharField(max_length=30,null=True)
    updated_by = models.CharField(max_length=30,null=True)
    
    
    

# Create your models here.
