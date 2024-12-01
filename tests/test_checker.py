from healthcheck.checker import check_url


def test_check_url():
    result = check_url("https://example.com")
    assert "url" in result
    assert "status_code" in result or "error" in result
