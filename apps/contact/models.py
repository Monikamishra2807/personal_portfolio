from django.db import models
from apps.common.models import TimeStampedModel
class ContactSubmission(TimeStampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False, db_index=True)
    def __str__(self): return self.subject
