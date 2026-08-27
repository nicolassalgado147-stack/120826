import requests

def test_get_root_200_ok():
    url = "http://localhost:5050/"
    response = requests.get(url)
    assert response.status_code == 200, f"Se esperaba 200 OK pero se obtuvo {response.status_code}"