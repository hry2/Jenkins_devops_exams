import os
import httpx

DEFAULT_CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/casts/'

async def is_cast_present(cast_id: int) -> bool:
    url = os.environ.get('CAST_SERVICE_HOST_URL', DEFAULT_CAST_SERVICE_HOST_URL)
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f'{url}{cast_id}')
            return r.status_code == 200
    except Exception as e:
        print(f"[ERROR] Failed to contact cast-service: {e}")
        return False
