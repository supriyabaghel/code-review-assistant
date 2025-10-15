from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class FileInfo(BaseModel):
    filename: str
    language: str
    size: int


class Issue(BaseModel):
    file: str
    line: Optional[int] = None
    severity: str
    message: str
    suggested_fix: Optional[str] = None
    confidence: Optional[float] = None


class Suggestion(BaseModel):
    category: str
    message: str


class Metrics(BaseModel):
    readability_score: float


class Analysis(BaseModel):
    summary: str
    issues: List[Issue]
    suggestions: List[Suggestion]
    metrics: Metrics


class ReportResponse(BaseModel):
    id: str
    status: str
    report: Dict[str, Any]
