from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.permissions import role_required

from .models import User

DASHBOARDS = {
    User.Role.SCHOOL_ADMIN: "school_admin_dashboard",
    User.Role.PARENT: "parent_dashboard",
    User.Role.DRIVER: "driver_dashboard",
    User.Role.MARSHAL: "marshal_dashboard",
}


@login_required
def home(request):
    """Send each user to the dashboard for their role."""
    if request.user.is_superuser:
        return redirect("admin:index")
    return redirect(DASHBOARDS[request.user.role])


@role_required(User.Role.SCHOOL_ADMIN)
def school_admin_dashboard(request):
    return render(request, "admin/dashboard.html")


@role_required(User.Role.PARENT)
def parent_dashboard(request):
    return render(request, "parent/dashboard.html")


@role_required(User.Role.DRIVER)
def driver_dashboard(request):
    return render(request, "driver/dashboard.html")


@role_required(User.Role.MARSHAL)
def marshal_dashboard(request):
    return render(request, "marshal/dashboard.html")
