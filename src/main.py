import uvicorn
from fastapi import FastAPI

from src.web_page.router import router as web_page_router

app = FastAPI(title='Web Page Analyser')

app.include_router(web_page_router)

if __name__ == '__main__':
    uvicorn.run('src.main:app', host='127.0.0.1', log_level='info')
