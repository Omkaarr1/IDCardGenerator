from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os
import subprocess

app = FastAPI()

UPLOAD_FOLDER = 'static/uploads'
PROCESSED_IMAGE = 'static/output_image.png'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def upload_file(
    request: Request,
    name1: str = Form(...),
    name2: str = Form(...),
    name3: str = Form(...),
    image: UploadFile = File(...)
):
    # Save image
    image_path = os.path.join(UPLOAD_FOLDER, 'uploaded_image.png')
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    # Process image with two Python scripts
    subprocess.run(['python', 'process_image_1.py'])
    subprocess.run(['python', 'process_image_2.py', name1, name2, name3])
    
    return RedirectResponse(url="/download", status_code=303)

@app.get("/download")
async def download_file():
    return FileResponse(PROCESSED_IMAGE, media_type='application/octet-stream', filename='output_image.png')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
