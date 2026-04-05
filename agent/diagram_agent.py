from agent.llm import call_llm

def generate_diagram(topic, title):
    prompt = f"""
Create a visual flow diagram for a slide.

Topic: {topic}
Slide: {title}

Return 3–5 short labels (1–3 words each)
that represent meaningful flow.

If diagram is NOT suitable, return: NONE
"""

    response = call_llm(prompt)

    if "NONE" in response:
        return None

    steps = [x.strip() for x in response.split("\n") if x.strip()]
    return steps[:5]