from django.urls import path

from . import views

urlpatterns = [
    path('search', views.index, name='index'),
    path('pic', views.pic, name='pic'),
    path('bake', views.bake, name='bake'),
    path('ajax-template', views.ajax_template, name='ajax-template'),
    path('ajax-demo', views.ajax_demo, name='ajax-demo'),
    path('auth', views.auth, name='auth'),
]