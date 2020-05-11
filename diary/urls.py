from django.urls import path, re_path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    re_path(r'^subjects/(?P<subject_id>\d+)/$', views.subject, name='subject'),
]
