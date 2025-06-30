from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()
students={
    1: {"name": "Surya", 
        "age": 22,
        "city": "Tirupati"},
    2: {"name": "Adithya", 
        "age": 21, 
        "city": "Satyavedu"},
    3: {"name": "Akshaya", 
        "age": 21, 
        "city": "Nellore"}
}
class Student(BaseModel):
    name:str
    age:int
    city:str
class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    city:Optional[str]=None    
@app.get("/")
def Hell():
    return {"Name":"Surya"}
@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(description="The ID of the student you want to view")):
    return students[student_id]    
#gt greater than, lt less than, ge greater than or equals, le
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int,name: Optional[str]=None, test: int):
    name = name.lower()
    for student_id in students:
        if students[student_id]["name"].lower() == name:
            return students[student_id]
    return {"error": "no such student found!"}
@app.post("/create-student/{student_id}")
def create_student(student_id: int, stud:Student):
    if student_id in students:
        return {"error": "Record already exists."}
    students[student_id]=stud
    return students[student_id]
#PUT
@app.put("/update-student/{student-id}")
def update_student(student_id: int,stud: UpdateStudent):
    if student_id not in students:
        return {"error":"Record doesnot exists"}
    if stud.name !=None:
        students[student_id].name=stud.name
    if stud.age !=None:
        students[student_id].age=stud.age    
    if stud.city !=None:
        students[student_id].city=stud.city
    return students[student_id]
@app.delete("/delete-student/{student_id}")
def del_student(student_id: int):
    if student_id not in students:
        return {"Error":"Record not found"}
    del students[student_id]
    return {"Message":"Record deleted successfully."}
