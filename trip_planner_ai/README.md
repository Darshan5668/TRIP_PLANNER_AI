# ✈️ AI Trip Planner (LangChain + Groq + Streamlit)

An end-to-end AI-powered trip planning application that dynamically orchestrates
multiple AI tools (OCR, Vision, and Trip Planning) using **LangChain** and **Groq LLMs**,
with both **CLI** and **Streamlit Web UI** support.

---

## 🚀 Features

- 🧠 **Multi-tool AI pipeline**
  - OCR tool for travel documents (tickets, menus, etc.)
  - Vision tool (optional) for place images
  - Trip Planner LLM that combines all inputs

- 🔁 **Automatic tool orchestration**
  - Tools are executed dynamically based on user input
  - OCR / Vision are optional, Trip Planner always runs

- 🌐 **Streamlit Web Interface**
  - Upload documents and images
  - Generate trip plans interactively

- 💻 **CLI Support**
  - Run the full pipeline from terminal

- 🔐 **Secure API key handling**
  - Uses environment variables (`GROQ_API_KEY`)
  - No hard-coded secrets

---

## 🧠 Architecture Overview

```text
User Input
   ↓
Decision Manager (manager.py)
   ↓
OCR Tool (optional) ──→ Structured OCR JSON
   ↓
Vision Tool (optional) ──→ Structured Vision JSON
   ↓
Trip Planner LLM
   ↓
Final Travel Itinerary

