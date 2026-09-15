# Import libraries
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path 
from agent import run_travel_agent

from pydantic import BaseModel, Field

import uvicorn 

# Define user input pydantic model schema
class UserInputSchema(BaseModel):
    user_query: str = Field(..., description="User query for travel planning")
    thread_id: str = Field(..., description="Thread ID for the conversation")

# Define fast api app 
app = FastAPI(
    title="TravelCrew AI",
    description="A Multi Agent AI Travel Trip Planner",
    version="1.0.0"
)

# Define templates
templates = Jinja2Templates(directory="templates")

# Create home route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

# Create API route for travel agent
@app.post("/travel")
async def travel_agent(input: UserInputSchema):
    try: 
        user_input = input.user_query.strip()
        thread_id = input.thread_id

        if not user_input:
            return JSONResponse(
                status_code=400,
                content={
                    "success":False,
                    "error":"User Input cannot be empty"
                    }
            )

        result = run_travel_agent(
            user_input=user_input,
            thread_id=thread_id
        )

        return JSONResponse(content={
            "success":True,
            "thread_id":result["thread_id"],
            "final_answer":result["final_answer"],
            "flight_result":result["flight_result"],
            "hotel_result":result["hotel_result"],
            "itinerary_result":result["itinerary_result"],
            "llm_call":result["llm_call"]
            })

    except Exception as e:
        print("Error:", e)

# Create health route 
@app.get("/health")
async def health():
    return {
        "status":"OK",
        "message":"TravelCrew - Multi AI Agent Travle Planner is running"
    }

@app.get("/favicon.ico")
async def favicon():
    return JSONResponse(content={})

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host = "127.0.0.1",
        port= 8000,
        reload=True
    )