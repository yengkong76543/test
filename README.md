# Law Insight

A simple law blog website with automatic browser fingerprinting.

## Features

- Clean, modern law blog interface
- Automatic browser fingerprinting on every visit
- Silent logging - no visible traces
- Ready for free hosting deployment

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:5000

## Deployment

### Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Done! Your site is live.

### Render

1. Connect your GitHub repo to Render
2. Select "Web Service"
3. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Environment: Python 3
4. Deploy!

### Railway

1. Connect GitHub repo
2. Railway auto-detects Python
3. Deploy!

## Fingerprinting

- **Automatic**: Runs silently when anyone visits your site
- **No UI**: No admin pages or visible endpoints
- **Logs**: Saved to `fingerprints/fingerprints_log.jsonl`
- **Data**: Each visit creates a JSON file with full browser fingerprint

## View Logs

After deployment, download logs from your hosting platform:
- **Vercel**: Use Vercel CLI: `vercel logs`
- **Render**: Download logs from dashboard
- **Railway**: View logs in dashboard

Or access server files directly if you have SSH access.

## Environment Variables (Optional)

Create `.env` file:
```
HOST=0.0.0.0
PORT=5000
DEBUG=False
```

## Notes

- Fingerprinting runs automatically - no user interaction needed
- All data is logged silently
- No admin interface - check log files directly
- Works on all free hosting platforms
"# test" 
