from database import TaskOrm, new_session
from schemas import STask, STaskAdd

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            
            task_orm = TaskOrm(**task_dict)
            session.add(task_orm)
            await session.flush()  # Ensure the ID is generated
            await session.commit()
            return task_orm.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            result = await session.execute(
                "SELECT id, name, description FROM tasks"
            )
            tasks = result.fetchall()
            task_schemas = [STask.model_validate(task) for task in tasks]
            return task_schemas