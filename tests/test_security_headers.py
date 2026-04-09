from src.app import create_app


def test_clickjacking_headers_present():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.get("/")
    assert response.headers.get("X-Frame-Options") == "DENY"
    assert "frame-ancestors 'none'" in response.headers.get("Content-Security-Policy", "")
