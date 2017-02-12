from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize, ResizeCanvas


# TODO make this a singleton?
class LandingPage(models.Model):
    photo = models.ImageField(upload_to='project_photos/')
    landing_page_photo = ImageSpecField(source='photo',
                                        processors=[SmartResize(2864, 1442)],
                                        format='JPEG',
                                        options={'quality': 60})
    thumbnail = ImageSpecField(source='photo',
                               processors=[SmartResize(400, 200)],
                               format='JPEG',
                               options={'quality': 60})

    class Meta:
        verbose_name_plural = 'Landing page'

    def __str__(self):
        return 'Landing page'


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    photo = models.ImageField(upload_to='project_photos/')
    thumbnail = ImageSpecField(source='photo',
                               processors=[SmartResize(400, 200)],
                               format='JPEG',
                               options={'quality': 60})
    text = models.TextField()

    class Meta:
        abstract = True


class AboutPage(Page):
    about_page_photo = ImageSpecField(source='photo',
                                      processors=[SmartResize(1110, 700)],
                                      format='JPEG',
                                      options={'quality': 60})


class Project(Page):
    display_order = models.IntegerField()
    architect = models.CharField(max_length=100)
    awards = models.TextField(blank=True)
    project_photo = ImageSpecField(source='photo',
                                   processors=[SmartResize(1110, 700)],
                                   format='JPEG',
                                   options={'quality': 60})
    photo_credit = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# TODO abstract repeated Photo code into MixIn?
class Photo(models.Model):
    PORTRAIT = 'P'
    LANDSCAPE = 'L'
    ORIENTATION_CHOICES = (
        (PORTRAIT, 'Portrait'),
        (LANDSCAPE, 'Landscape')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to='project_photos/')
    orientation = models.CharField(max_length=1, choices=ORIENTATION_CHOICES)
    display_order = models.IntegerField()
    portrait = ImageSpecField(source='photo',
                              processors=[SmartResize(500, 700), ResizeCanvas(1110, 700, color='black')],
                              format='JPEG',
                              options={'quality': 60})
    landscape = ImageSpecField(source='photo',
                               processors=[SmartResize(1110, 700)],
                               format='JPEG',
                               options={'quality': 60})
    thumbnail = ImageSpecField(source='photo',
                               processors=[SmartResize(400, 200)],
                               format='JPEG',
                               options={'quality': 60})
    credit = models.CharField(max_length=100)

    @property
    def is_landscape(self):
        return self.orientation == self.LANDSCAPE

    def __str__(self):
        return '{} {}'.format(self.project.title, self.pk)


class Press(models.Model):
    BOOK = 'B'
    MAGAZINE = 'M'
    PUBLICATION_TYPE_CHOICES = (
        (BOOK, 'Book'),
        (MAGAZINE, 'Magazine')
    )
    # TODO this should really be m2m in case multiple projects are in there
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, related_name='press')
    citation = models.CharField(max_length=200)
    publication_type = models.CharField(max_length=1, choices=PUBLICATION_TYPE_CHOICES)
    display_order = models.IntegerField()
    image = models.ImageField(upload_to='press/')
    pdf = models.FileField(upload_to='press/', blank=True)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Press'

    def __str__(self):
        return self.citation










