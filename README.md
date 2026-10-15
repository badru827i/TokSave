# TokSave

A lightweight, mobile-friendly TikTok downloader interface with a separate Python download engine.

## Features
- Responsive mobile-first UI
- Paste and validate HTTPS TikTok URLs
- Backend API built with FastAPI and yt-dlp
- `/health`, `/api/resolve`, and `/api/download` endpoints
- Render deployment blueprint at `render.yaml`

## Deploy the download engine
GitHub Pages hosts only the static frontend; it cannot run the Python engine.

1. In Render, create a new Blueprint and select this repository. Render will read `render.yaml` and create the `toksave-engine` service.
2. After deployment, open the service URL and confirm `/health` returns JSON with `"ok": true`.
3. Edit `index.html` and set `API_BASE` near the bottom to the full backend URL, for example `https://your-service.onrender.com` (no trailing slash required).
4. Commit the change and wait for GitHub Pages to redeploy.
5. Test with a public video URL you have permission to save.

## Notes
- The backend is code-complete but is **not deployed or connected automatically** by this repository change. Downloads will not work on the public page until steps above are completed.
- Free hosting may sleep between requests, and TikTok may change or restrict video extraction. This engine cannot guarantee every video will be downloadable.
- Do not add private API keys to `index.html`. Set `ALLOWED_ORIGINS` to the exact frontend origin if your published domain differs.
- Only save content you own or have permission to download, and respect creators' rights and platform terms.
