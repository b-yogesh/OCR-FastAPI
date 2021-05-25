import uvicorn

if __name__ == '__main__':
    uvicorn.run('ocr-app.app:app', port=7777, reload=True)