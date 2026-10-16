
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_api_schema():
    """Verify that the API schema is accessible."""
    response = client.get("/openapi.json")

    assert response.status_code == 200

    schema = response.json()
    assert "paths" in schema


def test_application_routes_are_available():
    """Verify that the URL shortener has registered API routes."""
    response = client.get("/openapi.json")

    assert response.status_code == 200

    paths = response.json()["paths"]

    assert len(paths) > 0


def test_unknown_route_returns_not_found():
    """Check that an unknown endpoint returns a 404 response."""
    response = client.get("/this-route-should-not-exist-12345")

    assert response.status_code == 404
