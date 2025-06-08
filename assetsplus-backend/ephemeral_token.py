from fastapi import FastAPI, HTTPException
import uvicorn
import httpx
import os

app = FastAPI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.post("/session")
async def get_ephemeral_token():
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/realtime/sessions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-realtime-preview-2025-06-03"
            }
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()
    
if __name__ == "__main__":
    uvicorn.run("ephemeral_token:app", host="127.0.0.1", port=8080, reload=True)