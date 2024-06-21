from typing import Callable

from fastapi import APIRouter, Depends, Request

from app.controllers import TaskController
from app.models.task import TaskPermission
from app.schemas.requests.tasks import TaskCreate
from app.schemas.responses.tasks import TaskResponse
from core.factory import Factory
from core.fastapi.dependencies.permissions import Permissions

task_router = APIRouter()


@task_router.get("/", response_model=list[TaskResponse])
async def get_tasks(
    request: Request,
    task_controller: TaskController = Depends(Factory().get_task_controller),
    assert_access: Callable = Depends(Permissions(TaskPermission.READ)),
) -> list[TaskResponse]:
    tasks = await task_controller.get_by_author_id(request.user.id)

    assert_access(tasks)
    return tasks