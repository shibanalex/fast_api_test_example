from contextlib import asynccontextmanager
from database import create_db, delete_db
from fastapi import FastAPI
from router import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield
    await delete_db()

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)