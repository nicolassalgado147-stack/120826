import requests

def test_get_root_200_ok():
    # Petición a la API local ANTES del despliegue
    # Si tu contenedor en docker-compose expone otro puerto (ej. 5058), cámbialo aquí
    url = "http://localhost:5050/"
    
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"Se esperaba 200, pero la API respondió con {response.status_code}"
    except requests.exceptions.ConnectionError:
        assert False, "No se pudo establecer conexión con la API en local."