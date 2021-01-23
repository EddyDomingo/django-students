from django.db import models

# Create your models here.

class ReportCard(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Email = models.EmailField()
    Math = models.IntegerField()
    English = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    First = '1st'
    Second = '2nd'
    Third = '3rd'
    Fourth = '4th'
    Fifth = '5th'
    grade = [
        (First, '1st'),
        (Second, '2nd'),
        (Third, '3rd'),
        (Fourth, '4th'),
        (Fifth, '5th'),
    ]
    year_in_school = models.CharField(
        max_length=3,
        choices=grade,
        default=First,
    )

    def __str__(self):
        return '{} {} {}'.format(self.Lname, ",", self.Fname)

