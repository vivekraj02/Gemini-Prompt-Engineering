def build_prompt(situation, tone):
    system = f"""You are an expert professional email writer. 
Tone: {tone}
Rules:
- Output format must be exactly: Subject: ...\n---\n[email body]
- Body max 120 words.
- Be direct, specific, and professional."""

    user = f"""Example:
Situation: Following up on TCS NQT interview from last week
Subject: Follow-up: TCS NQT Interview — Raj Vivek
---
Dear Hiring Team,
I appeared for the TCS NQT Digital assessment last week and wanted to follow up on my application status. I remain very interested in the opportunity.
Thank you for your time.

Now write an email for this situation: {situation}"""

    return system, user