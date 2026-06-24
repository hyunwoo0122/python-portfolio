from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret-key-12345":
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return x_api_key


@app.get("/users")
def get_users(
    api_key: str = Depends(verify_api_key)
):
    return {
        "users": ["user1", "user2"]
    }


@app.get("/items")
def get_items(
    api_key: str = Depends(verify_api_key)
):
    return {
        "items": ["item1", "item2"]
    }


@app.get("/public")
def get_public():
    return {
        "message": "public endpoint"
    }