from django.contrib import admin

from imagekit.admin import AdminThumbnail

from .models import LandingPage, AboutPage, Project, Photo, Press


class LandingPageAdmin(admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_display = ('__str__', 'admin_thumbnail')
    readonly_fields = (
        'admin_thumbnail',
    )


class PhotoInline(admin.TabularInline):
    model = Photo
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_display = ('__str__', 'admin_thumbnail')
    readonly_fields = (
        'admin_thumbnail',
    )
    fields = (
        'photo',
        'admin_thumbnail',
        'orientation',
        'display_order',
        'credit',
    )


class ProjectAdmin(admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    list_display = ('__str__', 'admin_thumbnail')
    readonly_fields = (
        'admin_thumbnail',
    )
    fields = (
        'title',
        'slug',
        'display_order',
        'photo',
        'admin_thumbnail',
        'photo_credit',
        'text',
        'architect',
        'awards',
    )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        PhotoInline,
    ]

admin.site.register(LandingPage, LandingPageAdmin)
admin.site.register(AboutPage)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Press)

