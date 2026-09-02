from fastapi import FastAPI,Request
from app.database import mongodb
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.auth import router as auth_router

app=FastAPI()


app.mount("/static",StaticFiles(directory="app/static"),
            name="static"
          )

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
         

app.include_router(auth_router)