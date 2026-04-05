from agent.llm import call_llm
from mcp_servers.ppt_server import PPTServer
from utils.logger import log
import json


def run_agent(topic):
    log("[AGENT] Starting autonomous PPT generation...")

    ppt = PPTServer()
    history = []

    max_slides = 5   # safety limit

    while True:
        prompt = f"""
You are an expert teacher creating a high-quality PowerPoint presentation.

Topic: {topic}

Slides created so far:
{history}

Your goal:
- Create engaging, meaningful slides
- Avoid generic content
- Ensure logical flow between slides

Rules:
- Each slide must have 3–4 bullet points
- Each bullet must be specific and informative
- Avoid vague words like "various", "important", "many"
- Use simple, clear language (school-level)

Actions:
1. CREATE_SLIDE → generate title, bullets, and type
2. FINISH → when presentation is complete

Slide types:
- text → explanation
- visual → image-focused
- mixed → text + image

Output STRICT JSON ONLY:

{{
  "action": "CREATE_SLIDE",
  "title": "Specific and meaningful slide title",
  "type": "text",
  "bullets": [
    "Clear explanation of concept",
    "Detailed insight or process",
    "Example or real-world fact",
    "Interesting takeaway"
  ]
}}

OR

{{
  "action": "FINISH"
}}
"""

        response = call_llm(prompt)
        log(f"[AGENT] Raw response: {response}")

        try:
            start = response.find("{")
            end = response.rfind("}") + 1
            data = json.loads(response[start:end])
        except:
            log("[AGENT] Invalid JSON, retrying...")
            continue

        
        if data.get("action") == "CREATE_SLIDE":
            title = data.get("title", "Untitled Slide")
            bullets = data.get("bullets", [])
            slide_type = data.get("type", "text")

            log(f"[AGENT] Creating slide: {title}")

            ppt.add_slide(
                title,
                bullets,
                slide_type,
                topic
            )

            history.append({
                "title": title,
                "type": slide_type,
                "bullets": bullets
            })

            if len(history) >= max_slides:
                log("[AGENT] Reached max slides")
                break

        elif data.get("action") == "FINISH":
            log("[AGENT] Finished by LLM decision")
            break

        else:
            log("[AGENT] Unknown action, retrying...")

    file = ppt.save()
    log(f"[AGENT] Saved: {file}")

def generate_plan(topic, num_slides=5):
    prompt = f"""
You are a presentation planner.

Create a structured outline for a {num_slides}-slide presentation on:
"{topic}"

Return ONLY valid JSON:

{{
  "slides": [
    "Slide 1 title",
    "Slide 2 title",
    "Slide 3 title"
  ]
}}
"""

    response = call_llm(prompt)

    try:
        data = json.loads(response)
        return data["slides"]
    except:
        print("[PLANNER] Failed, using fallback plan")
        return [
            "Introduction",
            "Overview",
            "Key Concepts",
            "Examples",
            "Conclusion"
        ]