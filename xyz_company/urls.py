
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

