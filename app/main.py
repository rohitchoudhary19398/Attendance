import uvicorn
from fastapi import FastAPI
from ctlogging.config import set_logger_from_yaml
from app.core.config import settings

set_logger_from_yaml(settings.LOG_YAML)

from app.api.v1.router import api_router


app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    from app import initialiser

    initialiser.init()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
