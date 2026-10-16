
from fastapi.testclient import TestClient
from app.main import app


def test_app_initializes():
    """Check that the FastAPI application initializes."""
    assert app is not None
    assert app.title


def test_app_routes_are_registered():
    """Check that the app has registered routes."""
    routes = [route.path for route in app.routes]

    assert len(routes) > 0


def test_openapi_schema_is_available():
    """Check that the application exposes its OpenAPI schema."""
    client = TestClient(app)

    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "paths" in response.json()
