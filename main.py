import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


load_dotenv(verbose=True)
api_key = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1")

async def stream_openai_chat(message: str):
    print("대화 시작 (종료하려면 '대화 종료' 입력)")
    
    messages=[
        {"role": "system", "content": "You are a helpful assistant for assets management."}
    ]

    while True:
        user_message = input("👤 사용자: ")

        if user_message.strip().lower() in ["exit", "quit"]:
            print("연결이 종료되었습니다.")
            break

        messages.append({"role": "user", "content": user_message})


        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True
        )

        async for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

        print()  # 줄바꿈

if __name__ == "__main__":
    user_message = input("👤 사용자 : ")
    asyncio.run(stream_openai_chat(user_message))