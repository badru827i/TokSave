# AI-FUSION Speed Test

Lightweight, responsive browser-based internet speed test prototype.

## Features
- Ping/latency estimate (median of five small requests)
- Download and upload throughput estimates
- Mobile-friendly dark UI
- Uses Cloudflare's public speed-test endpoint; a test consumes mobile data

## Publish with GitHub Pages
**One-time setup is required by the repository owner.** The GitHub Actions token cannot enable a Pages site when it has not been enabled for the repository yet.

1. Open **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions** and save if prompted.
3. Open **Actions → Deploy to GitHub Pages** and select **Run workflow** on branch `main`.
4. When deployment succeeds, open the Pages URL shown in the workflow run or in **Settings → Pages**.

After Pages has been enabled, pushes to `main` will trigger deployment automatically.

## Notes
This is a prototype, not a certified ISP benchmark. Results vary with signal quality, Wi-Fi, device load, server route and browser restrictions. Do not treat results as a guaranteed speed claim. A speed test uses real internet data.