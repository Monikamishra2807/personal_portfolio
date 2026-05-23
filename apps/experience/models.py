from django.db import models
from apps.common.models import TimeStampedModel, OrderedModel, PublishableModel
class Experience(OrderedModel, PublishableModel, TimeStampedModel):
    company = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    duration = models.CharField(max_length=120)
    responsibilities = models.TextField()
    tech_used = models.ManyToManyField('portfolio.TechStack', blank=True, related_name='experiences')
    def __str__(self): return f'{self.role} @ {self.company}'
