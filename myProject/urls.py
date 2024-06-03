from django.contrib import admin
from django.urls import path, include
from myApp import urls as myApp_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myApp/', include(myApp_urls)),          
]
