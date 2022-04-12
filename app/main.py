# app/main.py
from fastapi import FastAPI
from app.routers import control

app = FastAPI()
app.include_router(control.router)
