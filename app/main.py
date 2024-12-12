from fastapi import FastAPI
from .database import Base,engine
from .routers import router

#Initialize FastAPI
app = FastAPI()

#Initalize Database's Table
Base.metadata.create_all(bind=engine)

#Reguster Router
app.include_router(router=router, prefix="/api",tags=["todos"])