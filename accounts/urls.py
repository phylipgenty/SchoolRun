from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("school/", views.school_admin_dashboard, name="school_admin_dashboard"),
    path("parent/", views.parent_dashboard, name="parent_dashboard"),
    path("driver/", views.driver_dashboard, name="driver_dashboard"),
    path("marshal/", views.marshal_dashboard, name="marshal_dashboard"),
]
