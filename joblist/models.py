from django.db import models

GENDER_CHOICES = (
    ('Fulltime', 'Fulltime'),
    ('Parttime', 'Parttime'),
    ('Intership', 'Intership'),
    ('Remote', 'Remote'),
)
# Create your models here.


class Employer(models.Model):
    def __str__(self):
        return f"{self.topic}:{self.income}"

    create_at = models.DateTimeField(auto_now_add=True)
    type_job = models.CharField(choices=GENDER_CHOICES, max_length=100)
    country = models.CharField(max_length=30)
    income = models.IntegerField()
    topic = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='jobs/')

    summary1 = models.CharField(max_length=100)
    summary2 = models.CharField(max_length=100)
    summary3 = models.CharField(max_length=100)
    summary4 = models.CharField(max_length=100)
    summary5 = models.CharField(max_length=100)

    response1 = models.CharField(max_length=100)
    response2 = models.CharField(max_length=100)
    response3 = models.CharField(max_length=100)
    response4 = models.CharField(max_length=100)
    response5 = models.CharField(max_length=100)

    company1 = models.CharField(max_length=100)
    company2 = models.CharField(max_length=100)
    company3 = models.CharField(max_length=100)
    company4 = models.CharField(max_length=100)
    company5 = models.CharField(max_length=100)
