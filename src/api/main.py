import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from v1.routers import router

app = FastAPI()
app.include_router(router, prefix="/v1")

# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)
