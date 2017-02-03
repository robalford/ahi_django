from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Project, Photo


def portfolio_view(request):
    portfolio = get_list_or_404(Project)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio/portfolio.html', context)


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    main_photo = Photo.objects.get(project=project, main_photo=True)
    context = {'project': project, 'main_photo': main_photo}
    return render(request, 'portfolio/project.html', context)
