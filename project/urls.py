from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from project.settings import DEBUG

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    
    # INCLUDE APPS
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('', include('todo.urls')),
]

# INCLUDE STATIC
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# INCLUDE MEDIA
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if DEBUG:
    import debug_toolbar 
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]