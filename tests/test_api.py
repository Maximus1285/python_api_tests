

def test_get_facts_returns_200OK(api_client):
    """
    This test ensures that the API returns 200 OK
    """
    response = api_client.get("/facts")
    assert response.ok, "The response should be 200 OK"

def test_get_facts_returns_a_list(api_client):
    """
    This test ensures that the API returns a list of facts in a json format
    """
    response = api_client.get("/facts")
    response_body = response.json()
    assert isinstance(response_body, list), "The response should be a list"
    assert len(response_body) > 0, "The response should be a list with at least one item"

def test_facts_returns_correct_data(api_client, expected_facts):
    """
    This test ensures that the API returns the correct data
    """
    response = api_client.get("/facts")
    response_body = response.json()
    assert response_body == expected_facts, "The response should match the expected data"

def test_post_facts_returns_401Unauthorized(api_client):
    """
    This test is important. According to https://alexwohlbruck.github.io/cat-facts/docs/
    the /facts requires authentication. This test ensures that the API returns 401 Unauthorized
    """
    response = api_client.post("/facts")
    assert response.status_code == 401, "The /facts endpoint should return 401 Unauthorized"

def test_non_existing_endpoint_returns_404NotFound(api_client):
    """
    This test ensures that the API returns 404 Not Found
    """
    response = api_client.get("/facts1")
    assert response.status_code == 404, "The non-existing endpoint should return 404 Not Found"

def test_users_endpoint_returns_401Unauthorized(api_client):
    """
    This test is important. According to https://alexwohlbruck.github.io/cat-facts/docs/
    the /users requires authentication. This test ensures that the API returns 401 Unauthorized
    """
    response = api_client.get("/users")
    assert response.status_code == 401, "The /users endpoint should return 401 Unauthorized"
