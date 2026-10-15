# AI-FUSION Speed Test

Lightweight, responsive browser-based internet speed test prototype.

## Features
- Ping/latency estimate (median of five small requests)
- Download and upload throughput estimates
- Mobile-friendly dark UI
- Uses Cloudflare's public speed-test endpoint; a test consumes mobile data

## Publish with GitHub Pages
The repository includes a GitHub Actions workflow at `.github/workflows/pages.yml`.
1. Open **Settings → Pages** and ensure GitHub Actions is selected as the build/deployment source.
2. Push to `main` or run the workflow manually from **Actions**.
3. Open the Pages URL shown in the workflow deployment or Settings → Pages.

## Notes
This is a prototype, not a certified ISP benchmark. Results vary with signal quality, Wi-Fi, device load, server route and browser restrictions. Do not treat results as a guaranteed speed claim.