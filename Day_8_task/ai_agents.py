import requests
import ollama
import json

###### ------ claculator tool
## eval() is a python built-in function to calculate the expression
def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error in calculation"

###### ------ weather tool
##--- I have taken this api call from openweather api
API_KEY = "3c3b16657fb9dd1330b75821e3b30e92"
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        return f"{temp}°C"
    except:
        return "Weather data not available"

###### ------ LLM call
## --- here i used json format as a output for easy handing
def tool_agent(user_query):

    prompt = f"""
    You are an AI agent.
    
    Decide which tool to use based on the query.
    
    Available tools:
    1. calculator → for math
    2. weather → for weather info
    3.if the user query has a math expression return the math expression with matching tool alone and 
    if the user ask about what the weather in the particular place return the particular place and matching tool as input.
    
    Return ONLY JSON like:
    [
      {{"tool": "calculator", "input": "25*6"}},
      {{"tool": "weather", "input": "Chennai"}}
    ]
    Note : Do NOT include any explanations or extra text.
    
    User Query: {user_query}
    """

    response = ollama.chat(
        model="llama3:8b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']

###### ------ Tool choosing
def agent(user_query):
    llm_output = tool_agent(user_query)
    print(llm_output)
    decision = json.loads(llm_output)
    result =[]
    for d in decision:
        tool = d['tool']
        input = d['input']
        if tool == "calculator":
            res = calculator(input)
            result.append(f"{input} = {res}")
        elif tool == "weather":
            res = get_weather(input)
            result.append(f"Weather in {input} is {res}")
    return " and ".join(result)

###### ----- user query loop
while True:
    user_query = input("Please enter your query or enter 'q' to exit: ")
    if user_query.lower() in ["exit", "quit","q"]:
        break
    result = agent(user_query)
    print(result)

#eg query: What’s the weather in Madurai and calculate 34 * 8?