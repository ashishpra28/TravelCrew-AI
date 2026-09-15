# Import libraries
from langchain_groq import ChatGroq 
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage , BaseMessage

from langgraph.graph import StateGraph, START, END 
from typing import TypedDict, Annotated 
from langgraph.graph.message import add_messages
from langgraph.checkpoint.postgres import PostgresSaver

from tools.flight_tool import search_flights 
from tools.hotel_tool import search_hotels

from dotenv import load_dotenv

import os
import psycopg
import uuid

# Load dotenv 
load_dotenv()

# Define LLM
llm = ChatGroq(model="openai/gpt-oss-20b")

# Define database url 
DATABASE_URL = os.getenv("DATABASE_URL")

# Define state 
class TravelState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages] 
    user_query: str 
    flight_result: str 
    hotel_result: str 
    itinerary_result: str 
    llm_call: int 

# Create agent nodes: 

# flight agent node 
def flight_agent(state:TravelState): 
    # fetch user query 
    user_query = state["user_query"]

    # get flight data 
    flight_data = search_flights(user_query)

    # return 
    return {
        "flight_result":flight_data,
        "messages":[AIMessage(content=f"Flight result fetched from flight_search - {flight_data}")]
    }

# hotel agent node 
def hotel_agent(state:TravelState):
    # fetch user query 
    user_query = f"Best hotels for {state['user_query']}"

    # get hotel data 
    hotel_data = search_hotels(user_query)

    # return 
    return {
        "hotel_result": hotel_data, 
        "messages":[AIMessage(content=f"Hotel result fetched - {hotel_data}")]
    }

# itinerary agent node
def itinerary_agent(state: TravelState):

    # define prompt
    prompt = f"""
    Create a practical day-wise travel itinerary.

    User Query:
    {state['user_query']}

    Flight Results:
    {state['flight_result']}

    Hotel Results:
    {state['hotel_result']}
    """

    # llm response
    response = llm.invoke([
        SystemMessage(
            content="You are an expert travel planner."
        ),
        HumanMessage(content=prompt)
    ])

    # return
    return {
        "itinerary_result": response.content,
        "messages": [response],
        "llm_call": state.get("llm_call", 0) + 1
    }

# final agent node
def final_agent(state: TravelState):

    # final prompt 
    final_prompt = f"""
You are the final travel assistant.

Create a clean, practical travel plan for the user.

User Request:
{state['user_query']}

Flight Information:
{state['flight_result']}

Hotel Information:
{state['hotel_result']}

Itinerary:
{state['itinerary_result']}

Instructions:
- Give ONLY the final answer for the user.
- Do not mention agents, nodes, tools, state, or internal processing.
- Do not repeat raw search results.
- Do not invent exact flight schedules, prices, or hotel availability.
- Clearly separate flights, hotel suggestions, itinerary, and estimated budget.
- Keep the answer practical and easy to read.
- If the flight data is insufficient or unreliable, clearly say that exact flight availability needs to be checked.
"""

    # llm response
    response = llm.invoke([
        SystemMessage(
            content="You are a professional travel assistant who creates concise and reliable travel plans."
        ),
        HumanMessage(content=final_prompt)
    ])

    # return
    return {
        "messages": [response],
        "llm_call": state.get("llm_call", 0) + 1
    }

# Define graph
graph = StateGraph(TravelState)

# Add nodes
graph.add_node("flight_agent",flight_agent)
graph.add_node("hotel_agent",hotel_agent)
graph.add_node("itinerary_agent",itinerary_agent)
graph.add_node("final_agent",final_agent)

# Add Edges 
graph.add_edge(START,"flight_agent" )
graph.add_edge("flight_agent","hotel_agent")
graph.add_edge("hotel_agent","itinerary_agent")
graph.add_edge("itinerary_agent","final_agent")
graph.add_edge("final_agent",END)

# Define checkpoint 
conn = psycopg.connect(DATABASE_URL,autocommit=True)

checkpoint = PostgresSaver(conn)
checkpoint.setup() 

# Compile the graph 
travel_workflow = graph.compile(checkpointer=checkpoint)


# Define a function for run the agent 
def run_travel_agent(user_input:str, thread_id: str):
    if not thread_id:
        thread_id = f"user_{uuid.uuid4().hex}"

    config = {"configurable":{'thread_id':thread_id}}

    response = travel_workflow.invoke(
        {
            "messages": [
                {"role": "user", "content": user_input}
            ],
            "user_query": user_input,
            "flight_result":"",
            "hotel_result":"",
            "itinerary_result":"",
            "llm_call":0
        },
        config=config
    )

    # final answer 
    final_travel_plan_answer = response["messages"][-1].content

    # return 
    return {
        "thread_id":thread_id,
        "final_answer":final_travel_plan_answer,
        "flight_result":response.get("flight_result",""),
        "hotel_result":response.get("hotel_result",""),
        "itinerary_result":response.get("itinerary_result",""),
        "llm_call":response.get("llm_call",0),
    }

if __name__ == "__main__":

    user_input = input("Enter the trip plan: ")
    thread_id = "ashish2"

    result = run_travel_agent(user_input=user_input, thread_id=thread_id)

    print("\nFINAL RESPONSE\n")

    for mssg in result["messages"]:
        print(mssg.content)