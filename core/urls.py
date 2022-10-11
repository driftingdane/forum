
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', include('forum.urls', namespace='index')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "WakeUpDK Admin"
admin.site.site_title = "WakeUpDK Admin Portal"
admin.site.index_title = "Welcome to WakeUpDK"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
