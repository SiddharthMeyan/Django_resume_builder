from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    school = models.CharField(max_length=122,default="", editable=False)
    twelvep = models.CharField(max_length=7)
    tenthp = models.CharField(max_length=7)
    add = models.CharField(max_length=224,default="", editable=False)
    college = models.CharField(max_length=422,default="", editable=False)
    masters = models.CharField(max_length=422,default="", editable=False)
    tech = models.CharField(max_length=422,default="", editable=False)
    exp = models.CharField(max_length=422,default="", editable=False)
    skills = models.CharField(max_length=122,default="", editable=False)
    summary = models.TextField()

    def __str__(self):
        return self.name
    