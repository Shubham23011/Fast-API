from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional,List

app = FastAPI(
    title="Fast API Project",
    description="Management of students and their courses"
)

users = []

class User(BaseModel):
    email: str
    is_active : bool
    bio : Optional[str] = None

@app.get("/users",response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(
    id:int=Path(...,description="User ID",gt=2),
    query : str=Query(None,max_length=5)
    ):
    return {"user" :users[id], "query": query}