import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Problem(models.Model):
    problemId = models.IntegerField(primary_key=True)
    title = models.CharField(null=False, max_length=200)
    description = models.CharField(null=False, max_length=2000)
    difficulty = models.CharField(null=False, max_length=10)
    solved = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    topic = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.title


class Testcase(models.Model):
    problemId = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.CharField(null=False, max_length=1000)
    output = models.CharField(null=False, max_length=1000)

    def __str__(self):
        return self.problemId.title


class Submission(models.Model):
    problemId = models.ForeignKey(Problem, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.timezone)
    verdict = models.BooleanField()
