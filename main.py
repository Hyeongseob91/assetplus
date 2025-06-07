import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from utils import stream_openai_chat

app = FastAPI()

@app.websocket("/ws/chat")
async def chat_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        await websocket.send_text(f"사용자 ID를 입력하세요:")
        user_id = await websocket.receive_text()
        await websocket.send_text(f"사용자 {user_id}의 대화 시작 (종료하려면 '대화 종료' 입력)")
        await stream_openai_chat(user_id, websocket)

    except WebSocketDisconnect as e:
        logging.error(f"WebSocket 연결 오류 발생 {e}")
    except Exception as e:
        logging.error(f"예상치 못한 오류 발생: {e}")