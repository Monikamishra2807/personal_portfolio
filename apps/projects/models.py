from django.db import models
from apps.common.models import TimeStampedModel, OrderedModel, PublishableModel, SluggedModel
class ProjectTag(OrderedModel, PublishableModel, TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    def __str__(self): return self.name
class Project(OrderedModel, PublishableModel, TimeStampedModel, SluggedModel):
    title = models.CharField(max_length=200, db_index=True)
    short_description = models.CharField(max_length=240)
    description = models.TextField()
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True)
    video_demo = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    tech_stack = models.ManyToManyField('portfolio.TechStack', blank=True, related_name='projects')
    tags = models.ManyToManyField(ProjectTag, blank=True, related_name='projects')
    def __str__(self): return self.title
class ProjectImage(OrderedModel, TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='projects/gallery/', blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
