
from django.db import models
class blogs(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    subtitle=models.TextField()
    date=models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/wu.jpg')
    btntext=models.CharField(max_length=100)
    paragraph=models.TextField(default=False)
    def __str__(self):
        return self.title
class Index(models.Model):
    head = models.CharField(max_length=200)
    para = models.TextField()
    para2 = models.TextField()
    skills = models.TextField()
    softwares = models.TextField()
    mail = models.EmailField()
    image = models.ImageField(upload_to='images/', default='images/wu.jpg')
    def __str__(self):
        return self.head
