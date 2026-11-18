from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    template_name = "registration/login.html"

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("dashboard_redirect")

    def get_object(self):
        return self.request.user

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "registration/admin_dashboard.html"
    
    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMIN

class UserDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "registration/user_dashboard.html"

    def test_func(self):
        return self.request.user.role == CustomUser.Role.USER

class DashboardRedirectView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.role == CustomUser.Role.ADMIN:
            return redirect("admin_dashboard")
        return redirect("user_dashboard")