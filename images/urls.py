from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'images'

urlpatterns = [
    path('', views.image_list, name='list'),
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
