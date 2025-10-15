from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from .llm import review_code
from .storage import save_report, get_report, list_reports
from .schemas import ReportResponse, FileInfo
from .utils import detect_encoding

app = FastAPI(title="Code Review Assistant")

# Allow requests from anywhere (useful for frontend integration later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/review")
async def review_endpoint(file: UploadFile = File(...), language: Optional[str] = Form(None)):
    """
    Upload a source code file and get a review report.
    """
    filename = file.filename
    content = await file.read()

    # Detect encoding and decode file safely
    enc = detect_encoding(content)
    try:
        code_text = content.decode(enc)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not decode file as text")

    # Detect programming language from file extension if not provided
    lang = language or (filename.split('.')[-1] if '.' in filename else "unknown")

    # Analyze code using the LLM (or mock)
    analysis = await review_code(filename, lang, code_text)

    # Build report structure
    report = {
        "files": [{"filename": filename, "language": lang, "size": len(content)}],
        "analysis": analysis,
    }

    # Save report in memory (simple demo store)
    report_id = save_report(report)
    return {"id": report_id, "status": "done", "report": report}


@app.get("/report/{report_id}")
async def get_report_endpoint(report_id: str):
    """
    Retrieve a specific report by its ID.
    """
    r = get_report(report_id)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    return r


@app.get("/reports")
async def list_reports_endpoint():
    """
    List all generated reports.
    """
    return list_reports()
