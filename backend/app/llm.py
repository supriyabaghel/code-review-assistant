import os
import re
import json
from typing import Any, Dict
import httpx
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1/chat/completions")
MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")  
MOCK_LLM = os.getenv("MOCK_LLM", "false").lower() in ("1", "true", "yes")



def build_prompt(filename: str, language: str, code: str) -> str:
    return f"""
    You are an expert senior software engineer and code reviewer.
    File: {filename}
    Language: {language}

    Code:
    {code}

    Task:
    1. Summarize what this file does.
    2. List issues with approximate line numbers, severity (low/medium/high), and suggest fixes.
    3. Suggest improvements for readability, modularity, or performance.
    4. Rate readability on a scale of 1–10.
    5. Suggest 1–2 additional test cases.

    Output **only** a valid JSON object in this exact structure:

    {{
    "summary": "string",
    "issues": [
        {{
        "file": "{filename}",
        "line": null,
        "severity": "low|medium|high",
        "message": "string",
        "suggested_fix": "string",
        "confidence": 0.0
        }}
    ],
    "suggestions": [
        {{
        "category": "readability|performance|modularity",
        "message": "string"
        }}
    ],
    "metrics": {{
        "readability_score": 0.0
    }}
    }}
        """


async def call_llm(prompt: str, max_tokens: int = 1500) -> str:
       
        if MOCK_LLM:
            
            return json.dumps({
                "summary": "Mock summary: simple file purpose.",
                "issues": [],
                "suggestions": [
                    {"category": "readability", "message": "Consider renaming variables for clarity."}
                ],
                "metrics": {"readability_score": 7.5}
            })

        headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
        }

        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "max_tokens": max_tokens,
        }
        print("DEBUG OPENAI KEY PREFIX:", OPENAI_API_KEY[:8] if OPENAI_API_KEY else None) #sbadja
        print("DEBUG REQUEST HEADERS:", headers)
        print("DEBUG PROMPT LENGTH:", len(prompt))
        async with httpx.AsyncClient(timeout=60.0) as client:
            r = await client.post(OPENAI_API_URL, json=payload, headers=headers)
            print("DEBUG STATUS CODE:", r.status_code)
            print("DEBUG RAW RESPONSE:", r.text[:500])  # only first 500 chars
            r.raise_for_status()
            resp = r.json()


        
        try:
            content = resp["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            content = str(resp)

        return content


async def review_code(filename: str, language: str, code: str) -> Dict[str, Any]:
        
        prompt = build_prompt(filename, language, code)
        raw_output = await call_llm(prompt)

        
        match = re.search(r"\{[\s\S]*\}\s*$", raw_output)
        json_text = match.group(0) if match else raw_output

        try:
            data = json.loads(json_text)
        except Exception:
            data = {"parse_error": True, "raw": raw_output}

        
        data.setdefault("llm_metadata", {})
        data["llm_metadata"]["model"] = MODEL
        return data
