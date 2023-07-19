from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = "home" ),
    path('lenta', views.lenta , name = "lenta" ),
    path('signup' , views.signup.as_view() , name = 'signup'),
    path('Login' , views.Login , name = "Login"),
    path('endreg' , views.endreg , name = "endreg"),
    path('edit' , views.edit.as_view() , name = "edit"),
    path('password' , views.password_reset.as_view() , name = "password"),
    path('password2' , views.password_reset2.as_view() , name = "password2"),
    path('usersreset/<uidb64>/<token>/' , views.password_reset3.as_view() , name = "password3"),
    path('new_post' , views.new_post , name = "new_post"),
    path('premium' , views.premium , name = "premium"),
    #path('charge/', views.charge , name='charge'),
    ]
