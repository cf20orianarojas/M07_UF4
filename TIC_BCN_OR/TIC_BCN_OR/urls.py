from django.contrib import admin
from django.urls import path, include

# trucada a els paths de l'aplicació centre
urlpatterns = [
    path('admin/', admin.site.urls),
    path('centre/', include('centre.urls')),
]
