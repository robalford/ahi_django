from django.db import models
from django.utils.safestring import mark_safe

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize


class BaseImageProcessor(models.Model):
    photo = models.ImageField(upload_to='project_photos/')
    full_size = ImageSpecField(source='photo',
                               processors=[SmartResize(1200, 700)],
                               format='JPEG',
                               options={'quality': 80})
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    credit = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.photo.url))

    image_tag.short_description = 'Image'


class Project(BaseImageProcessor):
    project = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    architect = models.CharField(max_length=100)
    awards = models.TextField(blank=True)

    def __str__(self):
        return self.project


class Photo(BaseImageProcessor):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return '{} {}'.format(self.project.project, self.pk)








