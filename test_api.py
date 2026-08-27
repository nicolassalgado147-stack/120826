import requests
import time

def test_get_root_200_ok():
    url = "http://localhost:5050/"
    max_reintentos = 15
    pausa = 3

    # Reintenta conectarse durante 45 segundos mientras la API termina de iniciar
    for _ in range(max_reintentos):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                assert response.status_code == 200
                return
        except requests.exceptions.ConnectionError:
            time.sleep(pausa)

    # Intento final que mostrará el resultado exacto si no respondió a tiempo
    response = requests.get(url)
    assert response.status_code == 200