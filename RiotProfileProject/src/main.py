from fastapi import FastAPI
from BaseAPI import BaseAPI
import requests

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello": "world"}

@app.get("/test")
async def test():
    
    base_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/airWickedd2/NA1?api_key=RGAPI-75cd8c0b-66da-48ec-a8e4-33bd119a36a9"

    base = BaseAPI(base_url)
    # return requests.get(base_url)
    return base.get_response(base_url)
    
    # base.close()


if __name__=="__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)