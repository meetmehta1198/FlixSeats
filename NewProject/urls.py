"""NewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from movie import views
from booktickets.views import Selection,SelectTheatre,SelectMovie,SelectShow,Seat
#from booktickets.views import ShowMovies,ShowDetails,ShowTimings,Seat,Selection
urlpatterns = [
    url(r'^admin1/', admin.site.urls),
    url(r'^index/',views.index,name='index'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^special/',views.special,name='special'),
    url(r'^login/',views.user_login,name='user_login'), 
    url(r'^register/',views.register,name='register'),
    #url(r'^city',ShowCity.as_view(),name='city'),
    url(r'^select/',Selection,name='select'),
    url(r'^book/',SelectTheatre,name='theatre'),
    url(r'^movie/',SelectMovie,name='details'),
    url(r'^show/',SelectShow,name='show'),
    url(r'^seat/',Seat,name='seat'),
    url(r'^user_info/',views.user_profile,name='user_profile'),
    url(r'^update/(?P<pk>\d+)/',views.UserUpdate.as_view(),name='update'),
    #url(r'^seat/(?P<pk>\w+)/',Seat.as_view(),name='seats')
    url(r'^changepassword/',views.change_password,name='change_password')
    
]
