import os
import logging
from dotenv import load_dotenv
from openai import AsyncOpenAI
from fastapi import WebSocket

load_dotenv(verbose=True)
api_key = os.getenv("OPENAI_TEST_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1")

async def stream_openai_chat(websocket: WebSocket):
    messages=[{"role": "system", "content": "You are a helpful assistant for assets management."}]
    
    while True:
        user_message = await websocket.receive_text()
        if user_message.strip().lower() in ["대화 종료", "quit", "exit"]:
            await websocket.send_text("대화가 종료되었습니다.")
            break

        messages.append({"role": "user", "content": user_message})
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True
        )

        assistant_reply = ""
        async for chunk in response:
            if chunk.choices[0].delta.content:
                # print(chunk.choices[0].delta.content, end='', flush=True)
                assistant_reply += chunk.choices[0].delta.content
                
        messages.append({"role": "assistant", "content": assistant_reply})
        logging.info(assistant_reply)
        print(assistant_reply)
        await websocket.send_text(assistant_reply)