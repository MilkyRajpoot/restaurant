from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', views.register, name='register'),
    path('addFoodItem/', views.addFoodItem, name='addFoodItem'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('addAtribute/', views.addAtribute, name='addAtribute'),
# Ajax URL'S   
    # path('ajax/load-foodData/', views.load_foodData, name='ajax_load_foodData'),
]

