from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from example_app import views

router = routers.DefaultRouter()
router.register(r'baked_goods', views.BakedGoodViewSet)
router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    path('example_app/', include('example_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('pos/', include('pos.urls')),
]
