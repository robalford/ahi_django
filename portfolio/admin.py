from django.contrib import admin

from .models import Project, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    readonly_fields = (
        'image_tag',
    )
    fields = (
        'image_tag',
        'photo',
        'main_photo',
        'credit',
        'caption',
    )


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("project",)}
    inlines = [
        PhotoInline,
    ]

admin.site.register(Project, ProjectAdmin)

