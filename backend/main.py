import os
import re
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="TokSave Download Engine", version="1.0.0")

# Set ALLOWED_ORIGINS to the exact deployed TokSave site origin before production.
origins = [x.strip() for x in os.getenv("ALLOWED_ORIGINS", "https://badru827i.github.io").split(",") if x.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

class ResolveRequest(BaseModel):
    url: HttpUrl

def checked_url(raw: str) -> str:
    parsed = urlparse(raw)
    host = (parsed.hostname or "").lower().rstrip(".")
    allowed = host == "tiktok.com" or host.endswith(".tiktok.com")
    if parsed.scheme != "https" or not allowed or parsed.username or parsed.password:
        raise HTTPException(status_code=400, detail="Masukkan URL HTTPS TikTok yang sah.")
    return raw

def ydl_options():
    return {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "format": "best[ext=mp4]/best",
        "socket_timeout": 15,
        "retries": 1,
        "extractor_retries": 1,
    }

@app.get("/health")
def health():
    return {"ok": True, "service": "TokSave Download Engine"}

@app.post("/api/resolve")
def resolve(body: ResolveRequest):
    url = checked_url(str(body.url))
    try:
        with yt_dlp.YoutubeDL(ydl_options()) as ydl:
            info = ydl.extract_info(url, download=False)
        return {
            "ok": True,
            "title": info.get("title") or "TikTok video",
            "duration": info.get("duration"),
            "thumbnail": info.get("thumbnail"),
            "download_url": info.get("url"),
            "message": "Pautan video berjaya disediakan.",
        }
    except Exception:
        raise HTTPException(status_code=502, detail="Video tidak dapat diproses. Pastikan video awam dan cuba lagi.")

@app.post("/api/download")
def download(body: ResolveRequest):
    url = checked_url(str(body.url))
    temp_dir = tempfile.mkdtemp(prefix="toksave-")
    output = str(Path(temp_dir) / "video.%(ext)s")
    opts = ydl_options()
    opts.update({"outtmpl": output, "format": "best[ext=mp4]/best", "overwrites": True})
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = Path(ydl.prepare_filename(info))
        if not filename.exists():
            candidates = list(Path(temp_dir).glob("video.*"))
            if not candidates:
                raise RuntimeError("No output file")
            filename = candidates[0]
        title = re.sub(r"[^A-Za-z0-9._ -]", "", info.get("title") or "toksave-video").strip()
        title = (title[:80] or "toksave-video") + filename.suffix
        return FileResponse(
            path=str(filename),
            media_type="video/mp4" if filename.suffix.lower() == ".mp4" else "application/octet-stream",
            filename=title,
            background=None,
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=502, detail="Muat turun gagal. Video mungkin private, dipadam atau disekat oleh platform.")
