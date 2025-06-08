from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

# Setup static & templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Send image to processor service
    response = requests.post(
        "http://processor:5000/process/",
        files={"file": ("filename", image_bytes, file.content_type)}
    )

    with open("static/result.jpg", "wb") as f:
        f.write(response.content)

    app.mount("/static", StaticFiles(directory="static"), name="static")

    return {"processed_url": "/static/result.jpg"}
