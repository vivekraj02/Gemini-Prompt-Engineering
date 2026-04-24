def build_prompt(situation, tone):
    system = f"""You are an expert professional email writer. 
You must respond ONLY in JSON format with two keys: 'subject' and 'body'.
Tone: {tone}
Rules:
- 'body' must be max 120 words.
- Be direct, specific, and professional.
- Do not include any text outside the JSON object."""

    user = f"Write a professional email for this situation: {situation}"
    
    return system, user