from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.portfolio_view, name='portfolio'),
    url(r"^(?P<slug>[-\w]+)/$", views.project_view, name='project'),
]
