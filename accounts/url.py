
from django.urls import path 
from . import views              # النقطة تشير الى نفس الفولدر
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.logoutView.as_view(),name='logout')
    path('login/',auth_views.loginView.as_view(template_name='login.html'),name='login')
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change')
    path('settings/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done')


]