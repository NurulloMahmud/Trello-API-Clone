from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('projects.urls')),
    path('cart/', include('carts.urls')),
    path('task/', include('tasks.urls')),
]
