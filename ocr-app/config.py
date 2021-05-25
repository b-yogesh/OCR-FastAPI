from pydantic import BaseSettings


class Settings(BaseSettings):
    temp_dir: str = 'ocr-app/static/temp'
    folder: str = 'J:/PersonalProjects/ocr/'
    template_dir: str = "ocr-app/templates"
    static_dir: str = "ocr-app/static"

settings = Settings()