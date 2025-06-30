from fastapi import FastAPI,Path
app = FastAPI()
#GET this is used to retreive data/info
#POST this is used to create something new
#PUT this is used to update data/info/something 
#DELETE this is used to delete something
students ={
    1: {"name": "John", 
        "age": 20,
        "city": "New York"},
    2: {"name": "Jane", 
        "age": 22, 
        "city": "Los Angeles"},
    3: {"name": "Doe", 
        "age": 21, 
        "city": "Chicago"}
}
@app.get("/")
def index():
    return {"Name": "First Data"}
@app.get("/get-student/{student-id}")
def get_student(student_id: int=Query(None,description="the ID of the student you want to view")):
    return students[student_id]
