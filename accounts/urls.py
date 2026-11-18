from django.urls import path
from .views import (
    SignUpView, CustomLoginView, CustomLogoutView, 
    ProfileUpdateView, DashboardRedirectView, 
    AdminDashboardView, UserDashboardView
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("dashboard/", DashboardRedirectView.as_view(), name="dashboard_redirect"),
    path("dashboard/user/", UserDashboardView.as_view(), name="user_dashboard"),
    path("dashboard/admin/", AdminDashboardView.as_view(), name="admin_dashboard"),
]