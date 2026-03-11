from fastapi import FastAPI
from pydantic import BaseModel
import spacy

nlp = spacy.load("en_core_web_sm")# loadin the NLP modle form spacy lib.

food_calories = {
    "apple": 52,
    "banana": 89,
    "rice": 130,
    "chicken_breast": 165,
    "egg": 155,
    "milk": 42,
    "bread": 265,
    "potato": 77,
    "orange": 47,
    "paneer": 265
}
def estimate_daily_calories(text):
    doc = nlp(text)## this nlp model will split the text into tokens(individual words) and POS Tagging and find teh entity of the word.
    total_calories = 0
    for token in doc:
        if token.text.isdigit():
            quantity = int(token.text)
        food = token.text.lower()
        if food in food_calories:
            total_calories += quantity * food_calories[food]
    return total_calories

app1 = FastAPI()

class food_item(BaseModel):
    food_description : str

@app1.post("/Food_Calories_calculator")
def food_calories_calculator(data : food_item):
    calories = estimate_daily_calories(data.food_description)
    return {"estimated_calories": calories}
