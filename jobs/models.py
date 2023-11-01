from django.db import models
from joblist.models import Employer
# Create your models here.

GENDER_CHOICES = (
    ('Fulltime', 'Fulltime'),
    ('Parttime', 'Parttime'),
    ('Intership', 'Intership'),
    ('Remote', 'Remote'),

)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    about = models.TextField()
    picture = models.ImageField(upload_to="user/")

