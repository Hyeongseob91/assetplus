from fastapi import WebSocket, FastAPI
import os
import json
import requests
import aiohttp
import logging
import websockets
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

app = FastAPI()

response = requests.post("http://localhost:8080/session", headers={"X-Auth": "server-b-secret"})
response.raise_for_status()
API_KEY = response.json()["client_secret"]["value"]

# API_KEY = os.getenv("OPENAI_API_KEY")
REALTIME_URL = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2025-06-03"
HEADERS = [
    ("Authorization", f"Bearer {API_KEY}"),
    ("OpenAI-Beta", "realtime=v1")
]

# Tool 1: 보고서 요약
async def tool_report_summary(text: str, client_ws: WebSocket) -> None:
    async with websockets.connect(REALTIME_URL, header=HEADERS) as openai_ws:
        await openai_ws.send(json.dumps({
            "event": "conversation.item.create",
            "data": {
                "role": "user",
                "content": f"Please summarize the following financial report:\n\n{text}"
            }
        }))

        async for msg in openai_ws:
            data = json.loads(msg)
            if data.get("event") == "response":
                await client_ws.send_text(data["data"]["content"])
            if data.get("event") == "response.done":
                break

# Tool 2: 금융 뉴스 요약
async def scrape_financial_news() -> str:
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://news.naver.com/breakingnews/section/101/259"
        ]
        
        news_items = []
        for url in urls:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                articles = soup.select('.sa_text_strong')[:5]
                for article in articles:
                    title = article.text.strip()
                    link = article.find_parent('a')['href']
                    async with session.get(link) as detail_response:
                        detail_html = await detail_response.text()
                        detail_soup = BeautifulSoup(detail_html, 'html.parser')
                        description = detail_soup.select_one('#articleBodyContents').text.strip()
                    
                    news_items.append({
                        "title": title,
                        "description": description[:500] + "..."
                    })
        
        # 뉴스 데이터 포맷팅
        news_text = "오늘의 주요 경제 뉴스:\n\n"
        for item in news_items[:5]:
            news_text += f"- {item['title']}\n"
            news_text += f"  {item['description']}\n\n"
        
        return news_text

async def tool_finance_news(client_ws: WebSocket) -> None:
    try:
        news_text = await scrape_financial_news()   

        async with websockets.connect(REALTIME_URL, header=HEADERS) as openai_ws:
            await openai_ws.send(json.dumps({
                "event": "conversation.item.create",
                "data": {
                    "role": "user",
                    "content": f"링크로 접속하여 뉴스 헤드라인을 수집하고, 조회수가 높은 상위 5개의 기사를 요약해주세요:\n\n{news_text}"
                }
            }))

            async for msg in openai_ws:
                data = json.loads(msg)
                if data.get("event") == "response":
                    await client_ws.send_text(data["data"]["content"])
                if data.get("event") == "response.done":
                    break
    except Exception as e:
        print(f"Error 8{e}")


# Tool 3: 일반 상담
async def tool_general_chat(user_input: str, client_ws: WebSocket) -> None:
    async with websockets.connect(REALTIME_URL, additional_headers=HEADERS) as openai_ws:
        await openai_ws.send(json.dumps({
            "event": "conversation.item.create",
            "data": {
                "role": "user",
                "content": user_input}
        }
    )
)
        async for msg in openai_ws:
            logging.error(f"Error 9{msg}")
            data = json.loads(msg)
            if data.get("event") == "response":
                await client_ws.send_text(data["data"]["content"])
            if data.get("event") == "response.done":
                break