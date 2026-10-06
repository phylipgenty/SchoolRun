import pytest


@pytest.fixture(autouse=True)
def fast_password_hasher(settings):
    # The production hasher is deliberately slow; tests don't need that.
    settings.PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
