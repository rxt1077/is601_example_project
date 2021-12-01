from django.urls import path

from . import views

urlpatterns = [
    path('order', views.order, name='order'),
    path('show_order/<int:pk>', views.show_order, name='show_order'),
]