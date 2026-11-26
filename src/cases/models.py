from django.contrib.auth.models import User
from django.db import models

from config import settings


# Create your models here.
class Case(models.Model):
    class Status(models.TextChoices):
        FILED = "filed"
        HEARING = "hearing"
        CLOSED = "closed"

    number = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=Status, default=Status.FILED)
    filed_on = models.DateField(auto_now_add=True)
    people = models.ManyToManyField(User, through="CasePerson")


class CasePerson(models.Model):
    class Role(models.TextChoices):
        COMPLAINANT = "complainant"
        ACCUSED = "accused"
        LAWYER = "lawyer"
        WITNESS = "witness"
        JUDGE = "judge"

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="parties")
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role)
