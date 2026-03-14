import os

import pytest
from selenium import webdriver
from django.contrib.auth.models import User


@pytest.fixture(scope="session")
def base_url(live_server):
    return os.getenv("E2E_BASE_URL", live_server.url)


@pytest.fixture(scope="session")
def login_email():
    return os.getenv("E2E_LOGIN_EMAIL", "gmail@gmail.com")


@pytest.fixture(scope="session")
def login_password():
    return os.getenv("E2E_LOGIN_PASSWORD", "gmail")


@pytest.fixture
def existing_login_user(db, login_email, login_password):
    User.objects.filter(email=login_email).delete()
    user = User.objects.create_user(
        username=login_email,
        email=login_email,
        password=login_password,
    )

    yield user

    User.objects.filter(email=login_email).delete()

@pytest.fixture
def new_login_credentials(db):
    email = os.getenv("E2E_NEW_LOGIN_EMAIL", "azul@gmail.com")
    password = os.getenv("E2E_NEW_LOGIN_PASSWORD", "azul")

    User.objects.filter(email=email).delete()

    yield {
        "email": email,
        "password": password,
    }

    User.objects.filter(email=email).delete()

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
