from django.db import models

GENDER_CHOICES = (
   ('Fulltime', 'Fulltime'),
   ('Parttime', 'Parttime'),
   ('Intership', 'Intership'),
   ('Remote', 'Remote'),
)
# Create your models here.
class Employer(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    type_job=models.CharField(choices=GENDER_CHOICES,max_length=100)
    country=models.CharField(max_length=30)
    income = models.IntegerField()
    topic = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='jobs/')
    summary = models.TextField()
