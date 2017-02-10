from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Project, Photo, Press
from .imagegenerators import Portrait, Landscape, Thumbnail


def portfolio_view(request):
    portfolio = get_list_or_404(Project)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio/portfolio.html', context)


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {'project': project}
    return render(request, 'portfolio/project.html', context)


def recognition_view(request):
    press = get_list_or_404(Press)
    context = {'press': press}
    return render(request, 'portfolio/recognition.html', context)

