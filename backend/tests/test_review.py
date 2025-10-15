import asyncio
from httpx import AsyncClient
from app.main import app
import os




def test_review_endpoint(monkeypatch):
# Ensure mock mode
    os.environ['MOCK_LLM'] = 'true'


    async def _test():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            files = {"file": ("example.py", b"def foo():\n return 1\n")}
            resp = await ac.post("/review", files=files)
            assert resp.status_code == 200
            data = resp.json()
            assert "id" in data
            assert data["report"]["analysis"]["metrics"]["readability_score"] == 7.5


    asyncio.run(_test())