Auto PPT Agent
Overview

This project implements an AI-based Auto PPT Agent that automatically generates PowerPoint presentations from a single user prompt. The system uses an agentic workflow with tool integration (MCP-style) to create structured slides.

Features
Accepts a single prompt to generate a presentation
Automatically divides content into multiple slides
Generates slide titles and 3–5 bullet points
Uses a tool (PPTServer) to create and save .pptx files
Handles API failures with fallback content generation
Produces structured and readable presentations
Architecture

User Input → Agent → LLM → MCP Tool (PPTServer) → PowerPoint Output

Technologies Used
Python
Hugging Face API
python-pptx
Requests
Project Structure

auto-ppt-agent/
├── agent/
│ ├── llm.py
│ ├── orchestrator.py
│ ├── planner_agent.py
│ ├── writer_agent.py
│ └── prompts.py
├── mcp_servers/
│ └── ppt_server.py
├── config/
│ └── settings.py
├── utils/
│ ├── logger.py
│ └── parser.py
├── main.py
├── requirements.txt
└── README.md

How to Run
Install dependencies:
pip install -r requirements.txt
Create a .env file in the root directory:
HF_TOKEN=your_huggingface_token
HF_API_URL=https://router.huggingface.co/v1/chat/completions
Run the agent:
python main.py "Create a presentation on your topic"
Output
The generated PowerPoint file is saved in the output/ folder
File name includes timestamp
Error Handling
If the API fails (e.g., due to exhausted credits), the system generates fallback content
Ensures the presentation is always created without crashing
Demo

(Add your demo video link here)
