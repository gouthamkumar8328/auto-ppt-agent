PLANNER_PROMPT = """You are a presentation expert. Create a detailed slide plan for the following topic:

Topic: {topic}

Generate a JSON array with exactly 5 slides. Each slide must have a relevant title and 4-5 bullet points that are DIRECTLY RELATED to {topic}. Do not use generic placeholder content.

Return ONLY valid JSON. No other text. Example:
[
  {{
    "title": "Introduction to AI",
    "bullets": ["What is artificial intelligence", "Real-world applications", "Why AI matters today", "Key benefits"]
  }},
  {{
    "title": "Machine Learning Basics",
    "bullets": ["Supervised learning methods", "Unsupervised learning methods", "Training and validation", "Common use cases"]
  }},
  {{
    "title": "Neural Networks",
    "bullets": ["Network architecture", "Activation functions", "Backpropagation algorithm", "Deep learning frameworks"]
  }},
  {{
    "title": "Applications and Examples",
    "bullets": ["Natural language processing", "Computer vision", "Predictive analytics", "Recommendation systems"]
  }},
  {{
    "title": "Conclusion and Future",
    "bullets": ["Key takeaways", "Emerging trends", "Career opportunities", "Next steps for learning"]
  }}
]"""

PLANNER_PROMPT = """
You are a presentation planner.

Create a 5-slide presentation for the topic: {topic}

Return JSON format:
[
  {
    "title": "...",
    "type": "text | visual | diagram | mixed",
    "bullets": ["..."]
  }
]

Rules:
- text → explanation slides
- visual → image-heavy slides
- diagram → process/flow slides
- mixed → text + image
"""


WRITER_PROMPT = """
You are designing a professional presentation slide.

Topic: {topic}
Slide Title: {title}

Your job:
- Generate content that looks GOOD on slides
- Keep it clear, readable, and visually balanced
- Use short phrases or concise sentences where appropriate
- Avoid incomplete or broken text

Adapt style based on topic:
- Educational → simple explanation
- Technical → structured points
- Business → impactful keywords

Output only bullet points.
"""