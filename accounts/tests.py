import pytest
from django.urls import reverse

from accounts.models import User

ROLE_DASHBOARDS = [
    (User.Role.SCHOOL_ADMIN, "school_admin_dashboard"),
    (User.Role.PARENT, "parent_dashboard"),
    (User.Role.DRIVER, "driver_dashboard"),
    (User.Role.MARSHAL, "marshal_dashboard"),
]


def make_user(role, username=None):
    return User.objects.create_user(username=username or role, password="pw-12345!", role=role)


@pytest.mark.django_db
def test_new_user_defaults_to_parent():
    user = User.objects.create_user(username="ada", password="pw-12345!")
    assert user.role == User.Role.PARENT
    assert user.is_parent


@pytest.mark.django_db
def test_anonymous_home_redirects_to_login(client):
    response = client.get(reverse("home"))
    assert response.status_code == 302
    assert response.url.startswith(reverse("login"))


@pytest.mark.django_db
@pytest.mark.parametrize("role,dashboard", ROLE_DASHBOARDS)
def test_home_redirects_to_role_dashboard(client, role, dashboard):
    client.force_login(make_user(role))
    response = client.get(reverse("home"))
    assert response.url == reverse(dashboard)
    assert client.get(response.url).status_code == 200


@pytest.mark.django_db
def test_superuser_goes_to_django_admin(client):
    client.force_login(User.objects.create_superuser("root", "root@example.com", "pw-12345!"))
    assert client.get(reverse("home")).url == reverse("admin:index")


@pytest.mark.django_db
@pytest.mark.parametrize("role,_", ROLE_DASHBOARDS)
def test_other_roles_dashboards_are_forbidden(client, role, _):
    client.force_login(make_user(role))
    for other_role, dashboard in ROLE_DASHBOARDS:
        if other_role != role:
            assert client.get(reverse(dashboard)).status_code == 403


@pytest.mark.django_db
def test_login_with_password(client):
    make_user(User.Role.DRIVER, username="musa")
    response = client.post(reverse("login"), {"username": "musa", "password": "pw-12345!"})
    assert response.url == reverse("home")
