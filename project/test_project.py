import pytest
from project import validate_email, validate_password, validate_username


# ==============================================================================
# TESTS FOR validate_email
# ==============================================================================


def test_validate_email_valid():
    assert validate_email("user@example.com") is True
    assert validate_email("john.doe123@domain.co.uk") is True
    assert validate_email("student@harvard.edu") is True


def test_validate_email_invalid():
    assert validate_email("invalid-email") is False
    assert validate_email("user@.com") is False
    assert validate_email("@domain.com") is False
    assert validate_email("user@domain") is False
    assert validate_email("") is False
    assert validate_email(None) is False


# ==============================================================================
# TESTS FOR validate_password
# ==============================================================================


def test_validate_password_valid():
    assert validate_password("Valid123!") is True
    assert validate_password("P@ssw0rd2026") is True
    assert validate_password("Strong#Pass1") is True


def test_validate_password_invalid():
    # Too short (< 8 chars)
    assert validate_password("Short1!") is False
    # Missing uppercase letter
    assert validate_password("lowercase123!") is False
    # Missing lowercase letter
    assert validate_password("UPPERCASE123!") is False
    # Missing digit
    assert validate_password("NoNumbers!") is False
    # Missing special character
    assert validate_password("NoSpecial123") is False
    # Invalid types / empty
    assert validate_password("") is False
    assert validate_password(None) is False


# ==============================================================================
# TESTS FOR validate_username
# ==============================================================================


def test_validate_username_valid():
    assert validate_username("alice") is True
    assert validate_username("bob_123") is True
    assert validate_username("a" * 20) is True


def test_validate_username_invalid():
    # Empty string or whitespace only
    assert validate_username("") is False
    assert validate_username("   ") is False
    # Exceeds max length of 20 characters
    assert validate_username("a" * 21) is False
    assert validate_username(None) is False
