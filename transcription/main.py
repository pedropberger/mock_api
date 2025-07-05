
import random
import uuid
from fastapi import FastAPI
from pydantic import BaseModel, Field


class TranscriptionRequest(BaseModel):
    original_file_path: str
    user: str


class TranscriptionResponse(BaseModel):
    document_id: str
    transcription_text: str
    summary: str
    transcription_json: dict
    speakers: list
    confidence_score: float = Field(..., ge=0, le=1)
    processing_time_ms: int
    audio_duration_sec: int


app = FastAPI()


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe(request: TranscriptionRequest):
    return TranscriptionResponse(
        document_id=str(uuid.uuid4()),
        transcription_text="This is a sample transcription.",
        summary="This is a sample summary.",
        transcription_json={"text": "This is a sample transcription."},
        speakers=["speaker1", "speaker2"],
        confidence_score=random.uniform(0.9, 0.99),
        processing_time_ms=random.randint(5000, 30000),
        audio_duration_sec=random.randint(300, 600),
    )
