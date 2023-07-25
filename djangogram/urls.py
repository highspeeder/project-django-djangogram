from django.contrib import admin
from django.urls import path, include
from content.views import Main
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", Main.as_view()),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
