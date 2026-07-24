from django.db import models
from apps.common.models import TimeStampedModel, OrderedModel, PublishableModel
class Education(OrderedModel, PublishableModel, TimeStampedModel):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    year = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    def __str__(self): return f'{self.degree} - {self.institution}'
