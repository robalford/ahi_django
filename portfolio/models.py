from django.db import models
from django.utils.safestring import mark_safe

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize


class Project(models.Model):
    project = models.CharField(max_length=100)
    slug = models.SlugField()
    main_photo = models.ImageField(upload_to='main_photos/')
    main_photo_full_size = ImageSpecField(source='main_photo',
                                          processors=[SmartResize(1200, 800)],
                                          format='JPEG',
                                          options={'quality': 80})
    main_photo_thumbnail = ImageSpecField(source='main_photo',
                                          processors=[ResizeToFill(100, 50)],
                                          format='JPEG',
                                          options={'quality': 60})
    main_photo_credit = models.CharField(max_length=100)
    description = models.TextField()
    architect = models.CharField(max_length=100)
    awards = models.TextField(blank=True)

    def __str__(self):
        return self.project


def project_image_directory(instance, filename):
    return 'project_galleries/{}/{}'.format(instance.project.project, filename)


class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=project_image_directory)
    full_size = ImageSpecField(source='photo',
                               processors=[SmartResize(1200, 800)],
                               format='JPEG',
                               options={'quality': 80})
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    credit = models.CharField(max_length=100)
    caption = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return '{} {}'.format(self.project.project, self.pk)

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.photo.url))

    image_tag.short_description = 'Image'







