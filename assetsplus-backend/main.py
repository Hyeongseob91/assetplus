import logging
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from realtime_openai import tool_report_summary, tool_finance_news, tool_general_chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket 엔드포인트
@app.websocket("/ws/chat")
async def assetplus_chatbot_ws(websocket: WebSocket):
    await websocket.accept()
    print(f"WebSocket 연결됨: {websocket.client}")
    await websocket.send_text(f"이름을 입력해주세요.")
    user_id = await websocket.receive_text()
    await websocket.send_text(f"사용자 {user_id}님과 대화 시작 (종료하려면 '대화종료'를 입력하세요.)")
    await websocket.send_text(f"안녕하세요! {user_id}님! 저는 AssetPlus 챗봇입니다. ")
    await websocket.send_text("다음 기능들을 사용할 수 있습니다")
    await websocket.send_text("1. 보고서 요약")
    await websocket.send_text("2. 오늘의 주요 금융 뉴스 확인")
    await websocket.send_text("3. 일반 상담")
    await websocket.send_text("어떤 도움이 필요하신가요?")

    try:
        while True:
            user_input = await websocket.receive_text()
            logging.error(f"Error 1{user_input}")

            if user_input.strip() == '대화종료':
                logging.error(f"Error 2{user_input}")
                await websocket.send_text("대화를 종료합니다. 감사합니다!")
                break

            if '보고서' in user_input:
                logging.error(f"Error 3{user_input}")
                await websocket.send_text("요약할 보고서의 텍스트를 입력해주세요:")
                report_text = await websocket.receive_text()
                await tool_report_summary(report_text, websocket)

            elif '뉴스' in user_input:
                logging.error(f"Error 4{user_input}")
                await websocket.send_text("최신 금융 뉴스를 가져오는 중...")
                await tool_finance_news(websocket)

            else:
                logging.error(f"Error 5{user_input}")
                await tool_general_chat(user_input, websocket)

    except WebSocketDisconnect as e:
        logging.error(f"Error 6 {e}")
    except Exception as e:
        logging.error(f"Error 7: {e}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)