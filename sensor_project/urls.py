from django.contrib import admin
from django.urls import path, include
from sensors import views as myapp_views    
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sensors.urls')),
    path('', myapp_views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
