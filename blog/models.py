
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20,help_text="Post Title Here!")
    body=models.TextField(help_text="What do you think?")
    created_on= models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField('Category',related_name='posts')

    def __str__(self) -> str:
        return 'Name ' + str(self.title)

class Category(models.Model):
    name=models.TextField()
    
    def __str__(self) -> str:
        return 'Name ' + str(self.name)[0:20]

class Comment(models.Model):
    author=models.CharField(max_length=20)
    body=models.CharField(max_length=500)
    created_on=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return  str(self.body)[0:20]#slicing 
    