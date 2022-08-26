from operator import mod
from django.db import models
import random
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

def random_string_1():
    return str(random.randint(10000, 99999))

def random_string_2():
    return str(random.randint(1000, 9999))


class FactoryRecord(models.Model):
    COUNTRY_CHOICES = [
        ("VN", "Vietnam"),
        ("MY", "Malaysia"),
        ("PH", "Philippines"),
        ("SG", "Singapore"),
        ("TH", "Thailand"),
    ]
    factory_id = models.CharField(max_length=5,primary_key = True, unique=True, default = random_string_1, editable = False)
    org_id = models.CharField(max_length=4, default = random_string_2)
    country = models.CharField(max_length=10,choices=COUNTRY_CHOICES,default="VN", blank=True)
    execution_date = models.DateField(null=True, blank=True)
    fail_rate = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    defect_rate = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    # def __str__(self):
    #     return self.factory_id

    # class Meta:
    #     ordering = ['factory_id']