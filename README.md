# LLM-Powered Food Ordering Assistant

An autonomous agent-based proof-of-concept that lets you order food through a simulated messy UI using only natural language or voice. The agent orchestrates the interface, tracks your actions, and makes informed decisions on your behalf.

---

## ✨ Features
- **Autonomous UI Navigation:** Opens/closes pages, clicks buttons, and interprets UI elements.
- **Voice Interaction:** Accepts voice input and responds with speech.
- **Function Calling:** Maps natural language to backend functions.
- **Action Tracking:** Keeps memory of user actions to guide decision-making.
- **RAG-based Restaurant Search:** Uses embeddings + Pinecone for semantic restaurant search.

---

## 🚀 Quick Setup

### 1. Create a `.env`
- Get API keys from:
  - OpenAI
  - Pinecone (Index name: `auto-food-order`)
- Fill in [`.env.example`](./backend/.env.example) and rename it to `.env`

### 2. Create & Populate Database
- Follow the guide in [`backend/src/data/README.md`](./backend/src/data/README.md)
- Includes SQLite schema + Pinecone vector index

### 3. Configure the Model
- Edit [`config.yaml`](./backend/src/config/config.yaml)
- Recommended: `gpt-4` or `gpt-4-32k`

### 4. Run With Docker
```bash
docker compose up --build
```

---

## 🧳 How It Works

### 1. Data Sources
- Restaurant names, descriptions, items: **GPT-4 generated**
- Images: **DALL·E 3** via [`image_generator.ipynb`](./backend/src/images_generator/image_generator.ipynb)
- DBs:
  - SQL: **SQLite via SQLAlchemy**
  - Vector: **Pinecone** with OpenAI embeddings

### 2. Function Calling
- Backend maps each user action to a callable function
- All mappable functions defined in [`prompts`](./backend/src/prompts/) and [`services`](./backend/src/services/)

#### 2.1. RAG Restaurant Search
- Uses [LlamaIndex](https://github.com/run-llama/llama_index) + Pinecone
- Embedding: OpenAI
- Autonomous triggering when user requests a search

### 3. Services
- Backed by OpenAI + custom-defined services
- See [`services`](./backend/src/services/README.md)

### 4. Handlers
- Prepares and transforms data between services and frontend
- See [`handlers`](./backend/src/handlers/README.md)

### 5. Endpoints
- Receive frontend requests
- Use services + handlers
- Return transformed data to frontend
- See [`endpoints`](./backend/src/endpoints/README.md)

### 6. Frontend Orchestration

#### 6.1. Function Calling in Frontend
- Handled via [`handleFunctionCall`](./frontend/src/components/AppContainer.vue#312)
- If model returns a `function_call`, it is routed to UI-specific handler

#### 6.2. Action Tracking
- `registerAction()` in frontend logs actions like:
```js
this.actions.push("@action:" + msg + " at " + this.getCurrentTime())
```
- Chatbot can request these logs for better decisions
- Try asking: **"What did I just do?"**

---

## 🚜 Tech Stack
- **LLM:** OpenAI GPT-4
- **Database:** SQLite + Pinecone (Vector)
- **Backend:** Python (FastAPI style)
- **Frontend:** Vue.js
- **Dockerized**

