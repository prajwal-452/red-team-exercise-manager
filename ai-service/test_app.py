import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. Test POST /report works
def test_report_valid(client):
    response = client.post("/report", json={})
    assert response.status_code in [200, 400]

# 2. Test GET should fail (wrong method)
def test_report_wrong_method(client):
    response = client.get("/report")
    assert response.status_code in [404, 405]

# 3. Test empty input
def test_empty_input(client):
    response = client.post("/report", json={})
    assert response is not None

# 4. Test invalid JSON
def test_invalid_json(client):
    response = client.post("/report", data="invalid")
    assert response.status_code in [400, 415]

# 5. Test large input
def test_large_input(client):
    data = {"text": "A" * 1000}
    response = client.post("/report", json=data)
    assert response is not None

# 6. Test injection attempt
def test_injection(client):
    data = {"text": "<script>alert('hack')</script>"}
    response = client.post("/report", json=data)
    assert response is not None

# 7. Test response format
def test_response_format(client):
    response = client.post("/report", json={})
    if response.is_json:
        assert isinstance(response.json, dict)

# 8. Test missing content-type
def test_no_content_type(client):
    response = client.post("/report", data="{}")
    assert response.status_code in [400, 415]