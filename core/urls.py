from django.contrib import admin
from django.urls import path
from .views import hora,saludo2,edad_actual

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('hora',hora),
    path('saludo2',saludo2),
    path('edadactual',edad_actual),
    
]
