from django.db import models
from django.utils.text import slugify
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: abstract = True
class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0, db_index=True)
    class Meta: abstract = True; ordering = ['order', '-id']
class PublishableModel(models.Model):
    is_active = models.BooleanField(default=True, db_index=True)
    class Meta: abstract = True
class SluggedModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    slug_source_field = 'title'
    class Meta: abstract = True
    def save(self, *args, **kwargs):
        if not self.slug:
            source = getattr(self, self.slug_source_field, None)
            if source: self.slug = slugify(source)
        super().save(*args, **kwargs)
