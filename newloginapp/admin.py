from django.contrib import admin
from .models import students,marksheet



class stuadmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','img')
admin.site.register(students,stuadmin)
class marksdmin(admin.ModelAdmin):
    list_display = ('student','sub','mark')
admin.site.register(marksheet,marksdmin)


# Register your models here.
