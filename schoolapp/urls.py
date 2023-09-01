from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name='schoolapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('new/',views.new,name='new'),
    path('logout/',views.logout,name='logout'),
    path('form/',views.submitForm,name='form'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

]
