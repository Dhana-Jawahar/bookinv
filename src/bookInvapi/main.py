from fastapi import FastAPI, Depends, HTTPException, status
from .routers import bookcrud
from .routers import usercrud
from . import model 
from .log import logger
from .dbconn import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Inventory API")
logger.info("BookInvApi Started.....")
@app.get("/")
def HealthCheck():
    return {"message": "Book Inventory API is running..."}

app.include_router(usercrud.router)
app.include_router(bookcrud.router)
