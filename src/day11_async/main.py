import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/sync-fetch")
def sync_fetch():
    response = httpx.get("https://httpbin.org/delay/1")
    return response.json()


@app.get("/async-fetch")
async def async_fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://httpbin.org/delay/1"
        )

    return response.json()