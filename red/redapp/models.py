from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    Number_plate=models.CharField(max_length=15,primary_key=True)
    Name=models.CharField(max_length=10)
    Mobile_no=models.IntegerField()
    Address=models.TextField()
    Date=models.DateField()
    Day=models.CharField(max_length=15)
class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Number_plate","Name","Mobile_no","Address","Date","Day"]

