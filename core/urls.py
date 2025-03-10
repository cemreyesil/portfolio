from django.urls import path
from .views import index, projects,redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
path('link/<slug>/', redirect_urls, name='redirect_urls'),
]