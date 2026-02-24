from typing_extensions import Annotated
from fastapi import APIRouter

from repository import TaskRepository
from schemas import STaskAdd

task_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],  # советую добавить — будет красиво в Swagger
)

@task_router.post("/")
async def add_task(task: Annotated[STaskAdd, "Task to add"]):
    task_id = await TaskRepository.add_one(task)
    return {"message": "Task added successfully", "task_id": task_id}

@task_router.get("/")
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}