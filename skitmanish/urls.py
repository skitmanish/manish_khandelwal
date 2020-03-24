
from django.contrib import admin
from django.urls import path
from contact import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.detail,name='detail'),
    path('contact/',views.Contact,name='Contact'),
    
]
