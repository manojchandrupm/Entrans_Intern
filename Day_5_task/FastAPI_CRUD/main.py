from fastapi import FastAPI
from pydantic import BaseModel

class student(BaseModel):
    id : int
    name: str
    age: int
    place : str

app = FastAPI()

student_list = {}
###### creating_student_list.
@app.post("/students")
def create_student_list(student : student):
    student_list[student.id] = student
    return {"student_list": student_list}

###### Reading the student from the python dict database.
@app.get("/students/{student_id}")
def read_student_list(student_id: int):
    return student_list[student_id]

##### updating the existing student details using the id.
@app.put("/students/{student_id},{student_name}")
def update_student(student_id: int,student_name : str):
    # str_id = str(student_id)
    if student_id in student_list:
        student_list[student_id].name = student_name
        return {"message": "Student updated", "student_list": student_list}
    else:
        return {"message": f"Student with ID {student_id} not found."}

###### delete the student details
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student_list.pop(student_id)
    return {"message": "Student deleted"}

