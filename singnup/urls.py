"""singnup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mysignup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_up_view,name='signup'),
    path('login/',views.login_page_view,name='login'),
    path('profile/',views.profile_view,name='profile'),
    path('logout/',views.logout_view,name='logout'),
    path('changepass/',views.password_change_view,name='changepass'),
    path('setpass/',views.password_set_view,name='setpass'),
]
