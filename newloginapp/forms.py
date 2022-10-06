from django import forms 
from newloginapp.models import students,marksheet
  
class studentform(forms.ModelForm):  
    class Meta:  
        model = students  
        fields = ["id","first_name","last_name","img"]
class markform(forms.ModelForm):  
    class Meta:
        model = marksheet
        fields =["student","sub","mark"]
        ordering="student_id"
