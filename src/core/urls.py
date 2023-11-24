from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/main_page/', include('main_page.urls')),
                  path('api/v1/form/', include('form.urls'))

              ] + urls_swagger

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
