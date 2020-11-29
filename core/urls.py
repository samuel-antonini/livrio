from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'api/books', views.PubliViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('publication.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
