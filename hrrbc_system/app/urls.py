from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('pac_ativos', views.pac_ativos, name='pac_ativos'),
    
]
