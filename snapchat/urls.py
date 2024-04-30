
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('register/',register,name='register'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('jewellery/',login,name='jewellery'),
    path('shop Copy/',login,name='shop Copy'),
    path('shop/',login,name='shop'),
]
