import os
import json
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Load the variables from the .env file
load_dotenv()  

# 2. Setup the Client
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 3. Setting the specific 2.5 Flash model
MODEL = "gemini-2.5-flash" 

# Helper function to prevent "429 Resource Exhausted"
# 2.5 Flash requires slightly longer pauses than 2.0 on the free tier
def wait_a_bit():
    print("\n[System] Resting for 15 seconds to keep your Free Tier active...")
    time.sleep(15)

# ─────────────────────────────────────────
# TECHNIQUE 1: Zero-shot
# ─────────────────────────────────────────
print("\n--- TECHNIQUE 1: Zero-shot ---")
r = client.models.generate_content(
    model=MODEL,
    contents="Translate 'Hello, how are you?' into French."
)
print(r.text)
wait_a_bit()

# ─────────────────────────────────────────
# TECHNIQUE 2: Few-shot
# ─────────────────────────────────────────
print("\n--- TECHNIQUE 2: Few-shot ---")
few_shot_prompt = """Classify the sentiment of each review. Only reply with one word: Positive, Negative, or Neutral.

Review: "Absolutely loved it!" → Positive
Review: "Broke after 2 days." → Negative
Review: "It was okay." → Neutral

Review: "Fast delivery but the product smells weird." →"""

r = client.models.generate_content(
    model=MODEL,
    contents=few_shot_prompt
)
print(r.text)
wait_a_bit()

# ─────────────────────────────────────────
# TECHNIQUE 3: Chain-of-thought
# ─────────────────────────────────────────
print("\n--- TECHNIQUE 3: Chain-of-thought ---")
cot_prompt = """A train leaves Delhi at 6am going 80km/h.
Another leaves Mumbai at 8am going 100km/h.
Distance between the cities is 1400km.
When and where do they meet?

Think step by step."""

r = client.models.generate_content(
    model=MODEL,
    contents=cot_prompt
)
print(r.text)
wait_a_bit()

# ─────────────────────────────────────────
# TECHNIQUE 4: System prompt
# ─────────────────────────────────────────
print("\n--- TECHNIQUE 4: System prompt ---")
r = client.models.generate_content(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction="You are a senior backend engineer. Give concise answers only. Always mention time and space complexity for any code you write."
    ),
    contents="How do I find duplicates in a Python list?"
)
print(r.text)
wait_a_bit()

# ─────────────────────────────────────────
# TECHNIQUE 5: JSON output mode
# ─────────────────────────────────────────
print("\n--- TECHNIQUE 5: JSON output ---")
r = client.models.generate_content(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction="You are a data extractor. Respond ONLY with valid JSON. No explanation. No markdown backticks.",
        response_mime_type="application/json"   
    ),
    contents="Extract name, email, university from: Hi I'm Raj, raj@cu.ac.in, CS student at Chandigarh University."
)

data = json.loads(r.text)
print(data)
print(f"Name: {data.get('name')}")
print(f"Email: {data.get('email')}")

print("\n--- Morning Practice with 2.5 Flash Complete! ---")