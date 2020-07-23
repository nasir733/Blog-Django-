from django.db import models

# Create your models here.

# Create your models here.
# Database ----> Excel workbook
# Models In Django ----> Table  --------> Sheet

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=13)
    author = models.CharField(max_length=13)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' by '+ self.author