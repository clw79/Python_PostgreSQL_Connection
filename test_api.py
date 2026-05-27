import requests


def test_can_get_single_post_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
