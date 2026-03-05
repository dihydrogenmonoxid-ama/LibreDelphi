from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import Study
from .importer import import_participants

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):

    db: Session = SessionLocal()
    studies = db.query(Study).all()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "studies": studies},
    )


@app.post("/study/create")
async def create_study(title: str, description: str):

    db = SessionLocal()

    study = Study(
        title=title,
        description=description,
    )

    db.add(study)
    db.commit()

    return {"status": "ok"}


@app.post("/participants/import")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()

    with open("participants.xlsx", "wb") as f:
        f.write(contents)

    participants = import_participants("participants.xlsx")

    return {"imported": len(participants)}
