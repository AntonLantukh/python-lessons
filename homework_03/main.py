from fastapi import FastAPI
from views import user_router, status_router, ping_router

app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(status_router, prefix="/status", tags=["Status"])
app.include_router(ping_router, prefix="/ping", tags=["Ping"])
