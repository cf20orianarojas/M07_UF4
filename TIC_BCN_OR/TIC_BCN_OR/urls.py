from django.contrib import admin
from django.urls import path, include

# trucada a els path
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('centre/', include('centre.urls')),
    path('centre/students', include('centre.urls')),
    path('centre/teachers', include('centre.urls')),
]
