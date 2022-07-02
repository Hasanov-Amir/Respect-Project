from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('respectedfrontend.urls')),
    # path('', include('respectedapp.urls'))
]
