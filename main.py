from fastapi import FastAPI,Path,Query
# from pydantic import BaseModel
# from typing import Optional,List
from API import users,sections,courses


app = FastAPI(
    title="Fast API Project",
    description="Management of students and their courses"
)


app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
