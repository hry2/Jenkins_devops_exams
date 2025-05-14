import os
import httpx

# Valeur par défaut utilisable localement
DEFAULT_CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/casts/'

def is_cast_present(cast_id: int):
    url = os.environ.get('CAST_SERVICE_HOST_URL', DEFAULT_CAST_SERVICE_HOST_URL)
    r = httpx.get(f'{url}{cast_id}')
    return r.status_code == 200
