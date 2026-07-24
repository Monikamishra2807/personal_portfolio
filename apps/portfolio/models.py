from django.db import models
from apps.common.models import TimeStampedModel, OrderedModel, PublishableModel
class SocialLink(OrderedModel, PublishableModel, TimeStampedModel):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True)
    def __str__(self): return self.platform
class Profile(TimeStampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    tagline = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    experience_summary = models.TextField(blank=True)
    skills_summary = models.TextField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    is_available = models.BooleanField(default=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    def __str__(self): return self.name
class TechCategory(OrderedModel, PublishableModel, TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name
class TechStack(OrderedModel, PublishableModel, TimeStampedModel):
    category = models.ForeignKey(TechCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=120)
    level = models.PositiveSmallIntegerField(default=80)
    class Meta: unique_together = ('category', 'name')
    def __str__(self): return self.name
