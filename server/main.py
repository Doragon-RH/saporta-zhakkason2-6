from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import routers

app = FastAPI()
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routers.router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
        port=8888,
        log_level="debug"
    )
