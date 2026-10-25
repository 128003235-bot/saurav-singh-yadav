# Mrs Naaz Birthday Scrapbook

## Fix for photos not showing
This version automatically displays any JPG/JPEG/PNG/WEBP/GIF file inside `static/photos/`, regardless of its filename. Copy your photos into that folder, then restart the app.

Folder structure:
```
mrs_naaz_scrapbook_fixed/
  app.py
  requirements.txt
  static/
    photos/
      photo1.jpg
      photo2.jpg
      ...
    music/
```

## Run locally
```powershell
python -m pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000. Stop a running server with Ctrl+C before restarting.

## Publish online
Upload `app.py`, `requirements.txt`, and the complete `static` folder (including all photos and music) to GitHub. On Render use build command `pip install -r requirements.txt` and start command `gunicorn app:app`. Redeploy after adding photos online.
