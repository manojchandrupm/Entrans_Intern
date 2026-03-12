from fastapi import FastAPI
from sqlalchemy import create_engine

app = FastAPI()

engine = create_engine("sqlite:///students.db")