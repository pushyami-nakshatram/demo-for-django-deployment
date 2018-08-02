from django.urls import path
from learn_pwd import views

#TEMPLATE URLs
app_name = 'learn_pwd'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')

]
