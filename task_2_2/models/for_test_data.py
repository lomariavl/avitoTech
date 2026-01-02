from pydantic import BaseModel, Field


class ExistingTask(BaseModel):
    task_name: str = Field(alias='taskName')
    task_description: str = Field(alias='taskDescription')
    executor: str


class NewTask(BaseModel):
    task_name: str = Field(alias='taskName')
    task_description: str = Field(alias='taskDescription')
    status: str


class TestData(BaseModel):
    existing_task: ExistingTask = Field(alias='existingTask')
    new_task: NewTask = Field(alias='newTask')
