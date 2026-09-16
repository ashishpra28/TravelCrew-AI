# ✈️ TravelCrew AI

> A multi-agent AI travel planning assistant that combines flight search, hotel discovery, itinerary generation, and persistent conversation state into one workflow.

## 🌐 Live Demo

**Live Application:** https://travelcrew-ai.onrender.com/

---

## 📸 Application Preview

<img width="941" height="406" alt="image" src="https://github.com/user-attachments/assets/df2dead2-844c-4b18-bb6b-8a506f32d24d" />

---

## 🚀 Overview

**TravelCrew AI** is a multi-agent travel planning application built with **LangGraph, LangChain, FastAPI, PostgreSQL, and LLMs**.

Instead of handling the complete travel-planning task with a single LLM call, the application separates the workflow into specialized agents:

- ✈️ **Flight Agent** — searches for relevant flight information
- 🏨 **Hotel Agent** — finds hotel suggestions
- 🗺️ **Itinerary Agent** — creates a practical day-wise itinerary
- 🤖 **Final Agent** — combines the collected information into a clean travel plan

The workflow is orchestrated using **LangGraph**, while conversation state is persisted using **PostgreSQL checkpointing**.

---

## ✨ Features

- 🤖 Multi-agent travel planning workflow
- ✈️ Flight information search
- 🏨 Hotel discovery
- 🗺️ AI-generated day-wise itinerary
- 🧠 Persistent conversation state using PostgreSQL
- 🔗 Thread-based conversation management
- ⚡ FastAPI backend
- 🎨 Responsive web frontend
- ☁️ Production deployment
- 🔐 Environment-variable based API configuration
- 🐳 Docker support

---

## 🧠 Architecture

```text
                    User
                     │
                     ▼
              ┌──────────────┐
              │  FastAPI API │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   LangGraph  │
              │   Workflow   │
              └──────┬───────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Flight Agent  Hotel Agent  Itinerary Agent
        │            │            │
        ▼            ▼            ▼
   Flight Data    Hotel Data    AI Itinerary
        │            │            │
        └────────────┼────────────┘
                     ▼
              ┌──────────────┐
              │ Final Agent  │
              └──────┬───────┘
                     │
                     ▼
              Final Travel Plan
                     │
                     ▼
              PostgreSQL
          (Checkpoint / Memory)
```

<img width="410" height="302" alt="image" src="https://github.com/user-attachments/assets/af012cd2-2f52-4a13-b881-8757eb1584ed" />


---


### 1. Flight Agent

Receives the user's travel request and retrieves flight-related information using the flight search tool.

### 2. Hotel Agent

Uses the user's destination and travel request to search for relevant hotel options.

### 3. Itinerary Agent

Uses the user request, flight information, and hotel information to generate a practical day-wise itinerary using an LLM.

### 4. Final Agent

Combines the available information and produces the final response for the user in a clean and readable format.

---

## 🛠️ Tech Stack

### AI / LLM

- Python
- LangChain
- LangGraph
- Groq
- OpenAI-compatible LLM

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Database

- PostgreSQL
- `psycopg`
- LangGraph PostgreSQL Checkpoint

### External APIs / Tools

- Tavily Search
- AviationStack
- Python Requests

### Frontend

- HTML
- CSS
- JavaScript

### Deployment

- Render

---

## 📁 Project Structure

```text
TravelCrew-AI/
│
├── project_structure/
│   ├── workflow.excalidraw
│   └── workflow.png
│
├── templates/
│   └── index.html
│
├── tools/
│   ├── flight_tool.py
│   ├── hotel_tool.py
│
├── .dockerignore
├── .env
├── .gitignore
├── agent.py
├── app.py
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
```

> **Note:** `.env` contains secrets and should not be committed to GitHub. Add it to `.gitignore`.

---

## 🔮 Future Improvements

- 🔀 Parallel agent execution
- 🧭 Conditional routing
- 🔁 Iterative planning and refinement
- 💰 More detailed budget planning
- 🌦️ Weather-aware itinerary planning
- 🗺️ Maps and location integration
- ✈️ More structured real-time flight data
- 🏨 More structured hotel data
- 🧠 Better long-term travel preferences
- 📄 Downloadable travel plans
- 🔐 Authentication and user accounts
- 📊 Travel analytics and history

---

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

---
