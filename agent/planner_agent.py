import json
import re
from agent.llm import call_llm
from agent.prompts import PLANNER_PROMPT
from utils.logger import log


def extract_json_safe(text):
    try:
        match = re.search(r"\[\s*{.*}\s*\]", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        return None


def plan(topic):
    prompt = PLANNER_PROMPT.format(topic=topic)
    response = call_llm(prompt, topic=topic, slide_title="Planning")

    log(f"[PLANNER] Raw response: {response[:200] if response else 'empty'}")

    slides = extract_json_safe(response)

    if slides and len(slides) >= 3:
        log(f"[PLANNER] Parsed {len(slides)} slides from LLM")
        return slides

    log("[PLANNER] JSON parse failed → using smart fallback")

    return [
        {"title": f"Introduction to {topic}", "bullets": []},
        {"title": f"How {topic} Works", "bullets": []},
        {"title": f"Key Stages of {topic}", "bullets": []},
        {"title": f"Applications of {topic}", "bullets": []},
        {"title": f"Summary of {topic}", "bullets": []},
    ]