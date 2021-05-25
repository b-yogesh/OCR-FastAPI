from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from . import utils
from . import ocr

# Initialize fastapi instance
app = FastAPI()

# Initialize Jinja2 templates folder
templates = Jinja2Templates(directory="ocr-app/templates")

# Landing page URI
@app.get('/', tags=['root'])
def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.post("/perform_OCR")
def perform_OCR(image: UploadFile = File(...)):
    temp_file = utils.save_temp_file(image, path='temp')
    text = ocr.extract(temp_file)
    return {'text': text}

