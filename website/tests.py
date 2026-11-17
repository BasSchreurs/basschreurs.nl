from unittest.mock import patch

import pytest
from django.urls import reverse


def test_contact_invalid_post_shows_errors_and_keeps_input(client, mailoutbox):
    response = client.post(reverse("contact"), {
        "name": "Bas", "email": "not-an-email", "message": "",
    })

    form = response.context["form"]
    assert response.status_code == 200
    assert len(mailoutbox) == 0
    assert form.is_bound
    assert "email" in form.errors
    assert "message" in form.errors
    assert form["name"].value() == "Bas"  # typed input preserved


@patch("django.core.mail.message.EmailMessage.send", side_effect=Exception("SMTP down"))
def test_contact_email_failure_shows_error(mock_send, client):
    response = client.post(reverse("contact"), {
        "name": "Bas", "email": "visitor@example.com", "message": "Hello",
    })

    assert response.status_code == 200  # no redirect, no 500
    assert response.context["form"].non_field_errors()


def test_contact_get_renders_empty_form(client):
    response = client.get(reverse("contact"))
    assert response.status_code == 200
    assert not response.context["form"].is_bound

def test_contact_valid_post_sends_email_and_redirects(client, mailoutbox):
    response = client.post(reverse("contact"), {
        "name": "Bas",
        "email": "visitor@example.com",
        "message": "Hello there",
    })

    assert response.status_code == 302
    assert response.url == reverse("contact_success")
    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == "New message from Bas"
    assert mailoutbox[0].to == ["contact@basschreurs.nl"]
    assert "Hello there" in mailoutbox[0].body


@pytest.mark.parametrize("name", [
    "home", "about", "server_setup", "little_lemon",
    "dashboard", "motomeet", "bassinga", "contact", "contact_success",
])
def test_pages_return_200(client, name):
    assert client.get(reverse(name)).status_code == 200