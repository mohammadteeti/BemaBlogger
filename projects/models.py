from turtle import title
from django.db import models

from personal_portfolio.settings import STATIC_URL

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    image=models.FileField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    

    