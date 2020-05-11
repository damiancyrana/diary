from django.urls import path, re_path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    re_path(r'^subjects/(?P<subject_id>\d+)/$', views.subject, name='subject'),
    path('new_subject/', views.new_subject, name='new_subject'),
    re_path(r'^new_entry/(?P<subject_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
