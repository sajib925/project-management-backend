from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/issue/', include('users.urls')),
    path('api/issue/', include('issue.urls')),
    path('api/issue/', include('issueType.urls')),
    path('api/issue/', include('project.urls')),
    path('api/issue/', include('team.urls')),
    path('api/issue/', include('sprint.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)