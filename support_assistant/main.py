import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

MOCK_LLM = int(os.getenv("MOCK_LLM", 1))

class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float

app = FastAPI(title="Zepto Support Assistant API")

@app.post("/ask", response_model=AskResponse)
def ask_support(request: AskRequest):
    query = request.query.lower()
    keywords = ["delivery", "return", "refund", "membership", "tracking", "cancel", "gift card", "support hours"]
    
    is_policy = any(kw in query for kw in keywords)
    
    if MOCK_LLM == 1:
        if is_policy:
            answer = "Based on the retrieved context: Zepto delivers grocery and household essentials within 10 to 30 minutes..."
            sources = ["doc_01.txt"]
            confidence = 1.0
        else:
            answer = "I can only answer questions about Zepto policies right now."
            sources = []
            confidence = 1.0
    else:
        answer = "Real LLM response..."
        sources = ["doc_01.txt"]
        confidence = 0.95
        
    return AskResponse(answer=answer, sources=sources, confidence=confidence)
