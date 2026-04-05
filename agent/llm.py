import requests
import json
import os
from dotenv import load_dotenv
from utils.logger import log

load_dotenv()

HF_API_URL = os.getenv("HF_API_URL")
HF_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def call_llm(prompt, topic="", slide_title="", retries=3):
    """
    Calls Hugging Face Router API using chat-completions format.

    If API fails (credits exhausted, network error, etc),
    it falls back to local slide generation.

    Args:
        prompt (str): Input prompt for LLM
        topic (str): Topic of presentation
        slide_title (str): Current slide title (optional)
        retries (int): Number of retry attempts

    Returns:
        str: JSON string containing slide data
    """

    if not HF_API_URL or not HF_TOKEN:
        log("[LLM] Missing API config → using fallback")
        return generate_fallback_slide(topic, slide_title)

    for attempt in range(retries):
        try:
            log(f"[LLM] Calling {HF_API_URL} (Attempt {attempt+1})")

            response = requests.post(
                HF_API_URL,
                headers={
                    **HEADERS,
                    "Content-Type": "application/json"
                },
                json={
                    "model": "meta-llama/Llama-3.1-8B-Instruct",
                    "messages": [
                        {
                            "role": "system",
                            "content": "You generate structured presentation slides."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "max_tokens": 400,
                    "temperature": 0.7
                },
                timeout=30
            )

            log(f"[LLM] Status: {response.status_code}")

            if response.status_code == 200:
                data = response.json()

                if "choices" in data:
                    result = data["choices"][0]["message"]["content"].strip()
                    log(f"[LLM] Success: {result[:120]}")
                    return result
                else:
                    log(f"[LLM] Unexpected format: {data}")

            else:
                log(f"[LLM] HTTP Error {response.status_code}: {response.text}")

        except Exception as e:
            log(f"[LLM] Exception (attempt {attempt+1}): {str(e)}")

    log("[LLM] All attempts failed → using fallback content")
    return generate_fallback_slide(topic, slide_title)


def generate_fallback_slide(topic, slide_title):
    """
    Generates fallback slide content when LLM fails.

    Ensures the agent continues working even without API.

    Args:
        topic (str): Presentation topic
        slide_title (str): Slide title

    Returns:
        str: JSON string with slide content
    """

    title = slide_title if slide_title else f"{topic} Overview"

    fallback = {
        "action": "CREATE_SLIDE",
        "title": title,
        "type": "text",
        "bullets": [
            f"{topic} is an important concept to understand",
            "It involves key processes and ideas",
            "Examples help explain how it works",
            "Understanding this helps in real-world applications"
        ]
    }

    return json.dumps(fallback)


def render_local_plan(topic):
    """
    Generates a fallback 5-slide structured plan.

    Used when LLM is unavailable.

    Args:
        topic (str): Presentation topic

    Returns:
        list: List of slide dictionaries
    """

    topic_clean = topic.lower().replace(
        "create a 5-slide presentation on ", ""
    ).replace(" for a 6th-grade class", "").strip()

    return [
        {
            "title": f"Introduction to {topic_clean.title()}",
            "bullets": [
                f"What is {topic_clean}?",
                f"Why {topic_clean} is important",
                f"Key concepts to understand",
                f"Overview of the presentation"
            ]
        },
        {
            "title": f"Basic Concepts of {topic_clean.title()}",
            "bullets": [
                f"Fundamental principles of {topic_clean}",
                f"Important terms and definitions",
                f"How {topic_clean} works",
                f"Real-world examples"
            ]
        },
        {
            "title": f"Key Stages in {topic_clean.title()}",
            "bullets": [
                "Stage 1: Initial phase",
                "Stage 2: Development phase",
                "Stage 3: Main phase",
                "Stage 4: Final phase"
            ]
        },
        {
            "title": f"Applications of {topic_clean.title()}",
            "bullets": [
                f"Practical uses of {topic_clean}",
                "Examples from real life",
                "Impact on society",
                "Future possibilities"
            ]
        },
        {
            "title": f"Conclusion of {topic_clean.title()}",
            "bullets": [
                f"Key takeaways from {topic_clean}",
                "Summary of concepts",
                "Why it matters",
                "Final thoughts"
            ]
        }
    ]