import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import api_router
from core.config import settings 
from core.models import db_helper


# ##################################################################################################
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup    
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()
#######################################################################################################


app = FastAPI(
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.router_prefix.api)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app", 
        host=settings.run.host, 
        port=settings.run.port, 
        reload=True,
        )