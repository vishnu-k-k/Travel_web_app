from django.db import models
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descr=models.TextField()

def __str__(self):
    return self.name


