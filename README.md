# Auto PPT Agent

## Overview

This project is an AI-based Auto PPT Agent that generates PowerPoint presentations automatically from a single user prompt.
It uses an agent-based workflow and a PPT tool to create structured slides.

---

## Features

* Generates presentations from a single prompt
* Creates multiple slides automatically
* Adds title and 3–5 bullet points per slide
* Saves output as a `.pptx` file
* Handles API failure using fallback content

---

## Technologies Used

* Python
* Hugging Face API
* python-pptx

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file:
   HF_TOKEN=your_huggingface_token
   HF_API_URL=https://router.huggingface.co/v1/chat/completions

3. Run the program:
   python main.py "Create a presentation on your topic"

---

## Output

The generated PowerPoint file will be saved in the `output/` folder.

---

## Project Structure

auto-ppt-agent/
├── agent/
├── mcp_servers/
├── config/
├── utils/
├── main.py
├── requirements.txt

---

## Demo

https://drive.google.com/file/d/1k3vZPHSeZ9FbW3o8Xy0T9CJXrbCsL1in/view?usp=sharing
