"""CorrectionSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from CorrectionApp import views
from django.contrib.auth import views as auth_views
from CorrectionApp import forms
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=forms.LoginAuthForm), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^car_list', views.CarListView.as_view(), name='car_list'),
    url(r'^car/(?P<pk>\d+)/$', views.CarDetailView.as_view(), name='car-details'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url(r'^booking/(?P<car_pk>\d+)/$', views.BookingView.as_view(), name='booking')   `
