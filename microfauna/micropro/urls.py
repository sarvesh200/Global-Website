from django.conf.urls import url
from micropro import views
from micropro.forms import Userform,Userprofileinfo


app_name = 'micropro'


urlpatterns = [
              url(r'^register/$',views.register,name = 'register'),
              url(r'^userlogin/$',views.user_login,name = 'user_login')


]
