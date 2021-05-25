from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import utils, ocr, layoutlm
import os

TEMP_PATH =  'ocr-app/static/temp'
FOLDER = 'J:/PersonalProjects/ocr/'

# Initialize fastapi instance
app = FastAPI()

# Initialize Jinja2 templates folder
templates = Jinja2Templates(directory="ocr-app/templates")
app.mount("/static", StaticFiles(directory="ocr-app/static"))

# Landing page URI 
@app.get('/', tags=['root'])
async def index(request: Request):
    context = {"request": request}
    utils.remove_temp_files(FOLDER, TEMP_PATH)
    return templates.TemplateResponse("index.html", context)

@app.post("/perform_DAI")
async def perform_DAI(image: UploadFile = File(...)):
    temp_file = utils.save_temp_file(image, path='temp')
    is_success_ocr = ocr.extract(temp_file)
    if is_success_ocr:
        is_success_layout = layoutlm.get_layoutlm_predictions(temp_file)
    return {'is_success_ocr': is_success_ocr,
            'is_success_layout': is_success_layout}

