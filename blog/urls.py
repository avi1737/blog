"""blog URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
    path('register/',user_views.register,name='register'),
    path('Profile/',user_views.profile,name='profile'),
    path('Login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('Logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('reset-password', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
