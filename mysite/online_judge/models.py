from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField
    password = models.CharField
    total_score = models.IntegerField


class Problem(models.Model):
    problemId = models.IntegerField(primary_key=True)
    description = models.CharField
    difficulty = models.CharField
    solved_status = models.BooleanField(default=False)
    score = models.IntegerField


class TestCases(models.Model):
    problemId = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.CharField
    output = models.CharField


class Submission(models.Model):
    problemId = models.ForeignKey(Problem, on_delete=models.CASCADE)
    time = models.TimeField
    verdict = models.BooleanField
