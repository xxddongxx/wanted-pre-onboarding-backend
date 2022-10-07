from django.contrib.auth.models import AbstractUser
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobPost(models.Model):
    company = models.ForeignKey(Company, related_name="company", on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    compensation = models.IntegerField()
    content = models.TextField()
    stack = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.company.name}, {self.position}'

class User(models.Model):
    GENDER_M = "male"
    GENDER_F = "female"

    GENDER_CHOICE = (
        (GENDER_M, "Male"),
        (GENDER_F, "Female"),
    )

    name = models.CharField(max_length=20)
    birth = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} : {self.birth} - {self.age}'

class Application(models.Model):
    jobPost = models.ForeignKey(JobPost, related_name="jobPost", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)