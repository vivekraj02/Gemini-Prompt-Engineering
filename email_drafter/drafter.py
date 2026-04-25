import json
import os
import argparse
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import build_prompt

# Load API Key
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-2.5-flash"

def draft_email(situation, tone):
    system, user = build_prompt(situation, tone)
    
    r = client.models.generate_content(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=system,
            response_mime_type="application/json" # This is the magic JSON toggle
        ),
        contents=user
    )
    # Convert the raw JSON string from Gemini into a Python Dictionary
    return json.loads(r.text)

def save_output(email_data, filename):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%H%M%S")
    path = f"outputs/{filename}_{timestamp}.txt"
    
    with open(path, "w") as f:
        # We access the keys from the dictionary we got from Gemini
        f.write(f"SUBJECT: {email_data['subject']}\n")
        f.write("-" * 30 + "\n")
        f.write(email_data['body'])
    
    print(f"\n✅ JSON-structured Draft saved to: {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Email Drafter")
    parser.add_argument("--situation", required=True, help="Context of the email")
    parser.add_argument("--tone", default="professional", help="Tone (professional/friendly)")
    parser.add_argument("--save", default="draft", help="Filename prefix")
    
    args = parser.parse_args()
    
    print("\n🤖 Drafting your email...")
    result = draft_email(args.situation, args.tone)
    print(f"\nSubject: {result['subject']}")
    print(f"\nBody:\n{result['body']}")
    save_output(result, args.save)
