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
        'orientation',
        'credit',
    )


class ProjectAdmin(admin.ModelAdmin):
    fields = (
        'project',
        'slug',
        'photo',
        'image_tag',
        'orientation',
        'credit',
        'description',
        'architect',
        'awards',
    )
    prepopulated_fields = {"slug": ("project",)}
    readonly_fields = (
        'image_tag',
    )
    inlines = [
        PhotoInline,
    ]

admin.site.register(Project, ProjectAdmin)

