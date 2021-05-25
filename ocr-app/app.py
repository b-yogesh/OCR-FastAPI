from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import utils, ocr, layoutlm
import os
from . import config as app_config

TEMP_PATH =  app_config.settings.temp_dir
FOLDER = app_config.settings.folder

# Initialize fastapi instance
app = FastAPI()

# Initialize Jinja2 templates folder
templates = Jinja2Templates(directory=app_config.settings.template_dir)
app.mount("/static", StaticFiles(directory=app_config.settings.static_dir))

# Landing page URI 
@app.get('/', tags=['root'])
async def index(request: Request):
    context = {"request": request}
    utils.remove_temp_files(FOLDER, TEMP_PATH)
    return templates.TemplateResponse("index.html", context)

# Performs OCR + Document Sequence Labelling
@app.post("/perform_DAI")
async def perform_DAI(image: UploadFile = File(...)):
    temp_file = utils.save_temp_file(image, path='temp')
    is_success_ocr = ocr.extract(temp_file)
    if is_success_ocr:
        is_success_layout = layoutlm.get_layoutlm_predictions(temp_file)
    return {'is_success_ocr': is_success_ocr,
            'is_success_layout': is_success_layout}

