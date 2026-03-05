from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from workflow.langgraph_workflow import graph

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve PDF files
app.mount("/pdf_reports", StaticFiles(directory="pdf_reports"), name="pdf_reports")


@app.get("/")
def home():
    return {"message": "Agentic AI Data Analyst API running"}


@app.post("/ask")
async def ask_question(data: dict):

    question = data["question"]

    result = graph.invoke({
        "question": question
    })

    return {
        "sql_query": result.get("sql_query"),
        "pdf": result.get("pdf_file")
    }