from django.urls import path
from . import views

# отслеживание страниц
urlpatterns=[
   path('index', views.index, name='index'),
   path('about', views.about, name='about')
]