from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('', include('publication.urls')),
    path('api/v1/books/', views.PublicationList.as_view()),
    path('account/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
