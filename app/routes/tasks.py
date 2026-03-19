from fastapi import APIRouter, Depends, HTTPException
from app.core.deps import get_current_user
from app.db.mongo import tasks_collection
from app.schemas.task import TaskCreate
from bson import ObjectId

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate, user= Depends(get_current_user)):
    new_task = {
        "title": task.title,
        "completed": False,
        "user_id": user["_id"]
    }

    tasks_collection.insert_one(new_task)

    return {"message": "Task created"}

@router.get("/tasks")
def get_tasks(user=Depends(get_current_user)):
    tasks = list(tasks_collection.find({
        "user_id": user["_id"]
    }))

    # Convirtiendo _id
    for task in tasks:
        task["_id"] = str(task["_id"])
    
    return tasks

@router.patch("/tasks/{task_id}")
def complete_task(task_id: str, user= Depends(get_current_user)):
    result = tasks_collection.update_one(
        {
            "_id": ObjectId(task_id),
            "user_id": user["_id"]
        },
        {
            "$set": {"completed": True}
        }
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task completed"}

@router.delete("/task/{task_id}")
def delete_task(task_id: str, user= Depends(get_current_user)):
    result = tasks_collection.delete_one(
        {
            "_id": ObjectId(task_id),
            "user_id": user["_id"]
        }
    )

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task deleted"}


