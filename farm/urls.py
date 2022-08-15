from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('registration/',views.role_registrations,name='role_registration')
]
