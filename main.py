import sys
import re
from agent.orchestrator import run_agent


def extract_topic(user_input):
    text = user_input.lower()

    patterns = [
        r"create.*presentation on",
        r"make.*presentation on",
        r"give.*presentation on",
        r"ppt on",
        r"presentation on",
        r"slides on",
        r"explain",
        r"about",
    ]

    for p in patterns:
        text = re.sub(p, "", text)

    # remove slide count
    text = re.sub(r"\d+\s*slide[s]?", "", text)

    # remove "for beginners", "for kids"
    text = re.sub(r"for\s+.*", "", text)

    topic = text.strip()

    # fallback if empty
    if not topic:
        return user_input.strip()

    return topic.capitalize()


if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AI Basics"

    topic = extract_topic(user_input)

    print(f"[INFO] Extracted Topic: {topic}")  # debug

    run_agent(topic)