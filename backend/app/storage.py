from typing import Dict
import uuid
from datetime import datetime, timezone


# Simple in-memory store for demo. Replace with DB layer later.
STORE: Dict[str, Dict] = {}




def save_report(report: Dict) -> str:
    report_id = str(uuid.uuid4())
    report["id"] = report_id
    report.setdefault("created_at", datetime.now(timezone.utc).isoformat())
    STORE[report_id] = report
    return report_id




def get_report(report_id: str):
    return STORE.get(report_id)




def list_reports():
    return list(STORE.values())