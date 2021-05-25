from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import utils
from . import ocr

# Initialize fastapi instance
app = FastAPI()

# Initialize Jinja2 templates folder
templates = Jinja2Templates(directory="ocr-app/templates")
app.mount("/static", StaticFiles(directory="ocr-app/static"))

# Landing page URI 
@app.get('/', tags=['root'])
async def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.post("/perform_OCR")
async def perform_OCR(image: UploadFile = File(...)):
    temp_file = utils.save_temp_file(image, path='temp')
    is_success = ocr.extract(temp_file)
    return {'is_success': is_success}

