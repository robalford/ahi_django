from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Project(models.Model):
    project = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    architect = models.CharField(max_length=100)
    awards = models.TextField(blank=True)

    def __str__(self):
        return self.project


def project_image_directory(instance, filename):
    return 'projects/{}/{}'.format(instance.project.project, filename)


class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=project_image_directory)
    main_photo = models.BooleanField()
    credit = models.CharField(max_length=100)
    caption = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return '{} {}'.format(self.project.project, self.pk)

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.photo.url))

    image_tag.short_description = 'Image'






