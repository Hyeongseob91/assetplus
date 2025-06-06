from dotenv import load_dotenv
import os
import openai
import asyncio

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def stream_openai_response(message: str):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )

    async def event_generator():
        async for chunk in response:
            if "choices" in chunk:
                delta = chunk["choices"][0]["delta"]
                if "content" in delta:
                    yield f"data: {delta['content']}\n\n"
            await asyncio.sleep(0.01)

    return event_generator()