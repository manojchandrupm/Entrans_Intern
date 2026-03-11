from fastapi import FastAPI
from pydantic import BaseModel
from calorie_calculator import calculate_daily_calories

app = FastAPI()

###### creating the basemodel is used to build structure of input data,validate the data type, convert the json to python object
class CalorieRequest(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    exercise_days_per_week: int

###### if i start running the server, automatically the FastAPI will create the object(data) and allocate the each input value to it.
@app.post("/calculate")
def calculate_calories(data: CalorieRequest):
    calories = calculate_daily_calories(data.age, data.gender, data.height_cm, data.weight_kg, data.exercise_days_per_week)
    return {
        "Daily_calories": calories
    }