
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('tfk/', views.tfk, name="tfk"),
    path('mt/', views.mt, name="mt"),
    path('nti/', views.nti, name="nti"),
    path('kpa/', views.kpa, name="kpa"),
    

]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('fileLoad/', include('fileLoad.urls')),
#     path('', include('mainApp.urls')),
# ]