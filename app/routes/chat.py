from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.schema import ChatRequest
from app.services.openai_service import stream_openai_response

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    return StreamingResponse(stream_openai_response(request.message), media_type="text/event-stream")