# app/main.py
# Module 3: Intelligent AI Support Engine (RAG System) & FastAPI App

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Zepto AI Support Assistant")

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Welcome to the Zepto AI Support Assistant API!"}

@app.post("/ask")
def ask_support_assistant(request: QueryRequest):
    # TODO: Integrate your LangGraph / ChromaDB RAG logic here
    # to filter off-topic questions and answer based on official Zepto policy documents.
    
    user_question = request.question
    
    # Placeholder response
    return {
        "question": user_question,
        "answer": "This is a placeholder response from the Zepto RAG support assistant."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)