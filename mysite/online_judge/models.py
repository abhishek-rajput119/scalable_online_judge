import datetime

from django.db import models


# Create your models here.
class Problem(models.Model):
    problemId = models.IntegerField(primary_key=True)
    description = models.CharField(null=False, max_length=2000)
    difficulty = models.CharField(null=False, max_length=10)
    solved = models.BooleanField(default=False)
    score = models.IntegerField(default=0)


class Testcase(models.Model):
    problemId = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.CharField(null=False, max_length=1000)
    output = models.CharField(null=False, max_length=1000)


class Submission(models.Model):
    problemId = models.ForeignKey(Problem, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.timezone)
    verdict = models.BooleanField()
