from agent.llm import call_llm
from agent.prompts import WRITER_PROMPT
from utils.logger import log
import re

def write_slide(topic, title, fallback):
    prompt = WRITER_PROMPT.format(topic=topic, title=title)
    log(f"[WRITER] Generating content for: {title}")
    
    response = call_llm(prompt, topic=topic, slide_title=title)
    
    if not response or not response.strip():
        log(f"[WRITER] Empty response, using fallback")
        return fallback

    bullets = clean_bullets(response)

    if len(bullets) >= 3:
        log(f"[WRITER] Generated {len(bullets)} bullets")
        return bullets
    else:
        log(f"[WRITER] Only {len(bullets)} bullets, using fallback")
        return fallback

def clean_bullets(text):
    import re

    bullets = re.findall(r"(?:[-*•]|\d+\.)\s*(.*)", text)

    cleaned = []
    for b in bullets:
        b = b.replace("Slide:", "")   
        b = b.replace("*", "")        

        words = b.strip().split()
        short = " ".join(words[:5])   

        if short:
            cleaned.append(short)

    return cleaned[:4]