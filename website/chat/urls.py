from django.conf.urls import url
from django.template.backends import django

#from django.contrib.auth.views import login
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView
app_name = 'chat'

urlpatterns = [
    # login
    #url(r'^$', views.login, name="login"), # for admin interface

    # login/hell
    # url(r'^register/$', views.UserFormView.as_view(), name="register"),
    url(r'^$', views.UserFormView.as_view(), name="register"), # hit method in views.py


    url(r'login/^$', views.log_in.as_view(), {'template_name': 'templates/loginSuccess.html'}, name="login"),

   # url(r'^profile/$', views.loginSU, name="login"),

    url(r'/chat', views.index, name="chat"),    # after login - hits index.html
                                                # ask chat room id

    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),   # create room with respect to id

]