from app.agent.prompts import build_prompt

def generate_answer(query: str, context: str | None) -> str:
    prompt = build_prompt(query, context)
    # Call to LLM would go here
    # For demonstration purposes, I'll just return the prompt
    return prompt