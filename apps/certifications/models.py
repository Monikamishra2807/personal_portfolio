from django.db import models
from apps.common.models import TimeStampedModel, OrderedModel, PublishableModel
class Certification(OrderedModel, PublishableModel, TimeStampedModel):
    name = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150)
    issue_date = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)
    preview_image = models.ImageField(upload_to='certifications/', blank=True)
    def __str__(self): return self.name
