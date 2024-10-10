import pytest
from real_headers import real_headers, random_user_agent


def test_real_headers():
    fingerprint = real_headers()

    # Check if 'User-Agent' is in the fingerprint dictionary
    assert "User-Agent" in fingerprint, "User-Agent key should be present in the headers"

    # Check if the fingerprint is a dictionary
    assert isinstance(fingerprint, dict), "The returned fingerprint should be a dictionary"

    # Check if 'User-Agent' is not empty
    assert fingerprint["User-Agent"], "User-Agent should not be empty"

    # Check if the fingerprint has other values
    assert len(fingerprint) > 0, "Headers should contain other values"

    # Check if the returned User-Agent matches expected format (basic check)
    assert isinstance(fingerprint["User-Agent"], str), "User-Agent should be a string"


def test_random_user_agent():
    user_agent = random_user_agent()

    # Check if the result is a string
    assert isinstance(user_agent, str), "Random user agent should be a string"

    # Check if the user agent is not empty
    assert user_agent, "User-Agent should not be empty"
