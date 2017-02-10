from django.db import models
from django.utils.safestring import mark_safe

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail, SmartResize, ResizeCanvas


class BasePhoto(models.Model):
    PORTRAIT = 'P'
    LANDSCAPE = 'L'
    ORIENTATION_CHOICES = (
        (PORTRAIT, 'Portrait'),
        (LANDSCAPE, 'Landscape')
    )
    photo = models.ImageField(upload_to='project_photos/')
    orientation = models.CharField(max_length=1, choices=ORIENTATION_CHOICES)
    display_order = models.IntegerField()
    portrait = ImageSpecField(source='photo',
                              processors=[SmartResize(500, 700), ResizeCanvas(1110, 700, color='black')],
                              format='JPEG',
                              options={'quality': 80})
    landscape = ImageSpecField(source='photo',
                               processors=[SmartResize(1110, 700)],
                               format='JPEG',
                               options={'quality': 80})
    credit = models.CharField(max_length=100)

    class Meta:
        abstract = True

    @property
    def is_landscape(self):
        return self.orientation == self.LANDSCAPE

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="100" />'.format(self.photo.url))

    image_tag.short_description = 'Image'


class Project(BasePhoto):
    project = models.CharField(max_length=100)
    slug = models.SlugField()
    display_order = models.IntegerField()
    description = models.TextField()
    architect = models.CharField(max_length=100)
    awards = models.TextField(blank=True)

    def __str__(self):
        return self.project


class Photo(BasePhoto):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return '{} {}'.format(self.project.project, self.pk)


class Press(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, related_name='press')
    citation = models.CharField(max_length=200)
    display_order = models.IntegerField()
    image = models.ImageField(upload_to='press/')
    pdf = models.FileField(upload_to='press/', blank=True)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Press'

    def __str__(self):
        return self.citation










