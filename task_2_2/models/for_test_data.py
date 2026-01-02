from pydantic import BaseModel, Field


class ExistingTask(BaseModel):
    task_name: str = Field(alias='taskName')
    task_description: str = Field(alias='taskDescription')
    executor: str


class NewTask(BaseModel):
    task_name: str = Field(alias='taskName')
    task_description: str = Field(alias='taskDescription')
    project: str
    priority: str
    status: str
    executor: str


class FieldsForFillIn(BaseModel):
    name: str
    description: str
    project: str
    priority: str
    status: str
    executor: str
    create: str
    update: str


class TestData(BaseModel):
    existing_task: ExistingTask = Field(alias='existingTask')
    new_task: NewTask = Field(alias='newTask')
    fields_for_fill_in: FieldsForFillIn = Field(alias='fieldsForFillIn')
