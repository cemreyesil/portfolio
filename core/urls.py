from django.urls import path
from .views import index, projectsView, redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projectsView, name='projects'),
    path('link/<slug>/', redirect_urls, name='redirect_urls'),
]
