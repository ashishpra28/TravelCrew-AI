# ✈️ TravelCrew AI

> A multi-agent AI travel planning assistant that combines flight search, hotel discovery, itinerary generation, and persistent conversation state into one workflow.

## 🌐 Live Demo

**Live Application:** https://travelcrew-ai.onrender.com/

---

## 📸 Application Preview

<p align="center">
  <img src="![alt text](image.png)" alt="TravelCrew AI Frontend" width="100%">
</p>

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

---

## 🔄 Workflow

The current workflow follows a sequential multi-agent architecture:

```text
START
  │
  ▼
Flight Agent
  │
  ▼
Hotel Agent
  │
  ▼
Itinerary Agent
  │
  ▼
Final Agent
  │
  ▼
END
```

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
- Jinja2 Templates

### Deployment

- Render
- Vercel
- Docker

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
│   └── tavily_search.py
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
└── test.py
```

> **Note:** `.env` contains secrets and should not be committed to GitHub. Add it to `.gitignore`.

---

## 🔑 Environment Variables

For local development, create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATION_API_KEY=your_aviationstack_api_key
DATABASE_URL=your_postgresql_connection_string
DEFAULT_ORIGIN_IATA=DEL
```

For production, configure these variables in the hosting platform's environment-variable settings instead of committing them to the repository.

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ashishpra28/TravelCrew-AI.git
cd TravelCrew-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` with the variables shown above.

### 5. Run the application

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

### Health Check

```http
GET /health
```

### Travel Planning

```http
POST /travel
```

Example request:

```json
{
  "user_query": "Plan a trip from India to Japan for 7 days",
  "thread_id": "ashish2"
}
```

The API executes the LangGraph workflow and returns the generated travel plan along with workflow results.

---

## 🧠 Why LangGraph?

Travel planning naturally involves multiple steps and different responsibilities.

LangGraph provides a structured way to:

- Define shared application state
- Connect specialized agent nodes
- Control workflow execution
- Pass information between agents
- Persist state using checkpoints
- Maintain conversation threads
- Extend the workflow with conditional or parallel execution later

The current implementation uses a sequential graph, making the workflow easy to understand and extend.

---

## 💾 Persistence & Memory

TravelCrew AI uses **PostgreSQL** with LangGraph's PostgreSQL checkpointing system.

A `thread_id` is used to identify a conversation.

```text
User
 │
 ▼
thread_id
 │
 ▼
LangGraph
 │
 ▼
PostgreSQL Checkpoint
 │
 ▼
Persistent conversation state
```

---

## 🧪 Example

### User Request

```text
Plan a trip from India to Japan for 7 days.
```

### Workflow

```text
User Request
     ↓
Flight Search
     ↓
Hotel Search
     ↓
Itinerary Generation
     ↓
Final Travel Plan
```

---

## ☁️ Deployment

The application is deployed as a FastAPI application.

### Production URL

https://travelcrew-ai.onrender.com/

For production deployment, configure:

```text
GROQ_API_KEY
TAVILY_API_KEY
AVIATION_API_KEY
DATABASE_URL
DEFAULT_ORIGIN_IATA
```

The frontend uses a relative API endpoint:

```javascript
var API_BASE = "";
```

This allows the frontend to communicate with the FastAPI backend through the same deployed domain.

---

## 🐳 Docker

The project includes a `Dockerfile` for containerized deployment.

Build:

```bash
docker build -t travelcrew-ai .
```

Run:

```bash
docker run -p 8000:8000 travelcrew-ai
```

Then open:

```text
http://127.0.0.1:8000
```

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

## ⚠️ Disclaimer

TravelCrew AI is a portfolio project. Search results, flight information, hotel information, prices, availability, and itinerary suggestions may not always represent real-time or bookable information.

Always verify important travel details directly with airlines, hotels, and official travel providers before making a booking.

---

## 👨‍💻 Author

**Ashish Prajapati**  
BCA Student | Generative AI | Agentic AI | Data Science

GitHub: https://github.com/ashishpra28

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

---

<p align="center">
  Built with Python, LangGraph, LangChain, FastAPI, PostgreSQL & AI
</p>
