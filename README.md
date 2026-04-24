# Gemini-Prompt-Engineering

# Gemini Prompt Engineering Essentials 🚀

A structured practice repository focused on mastering LLM implementation using the **Google Gemini 2.5 Flash** model. This project demonstrates the core technical strategies required to transition from a "chatbot user" to an "AI Prompt Engineer."

## 📌 Project Overview
This repository documents a two-phase journey:
**Phase 1:** Mastering the 5 fundamental pillars of prompt engineering.
**Phase 2:** Building a production-ready CLI Email Drafter that utilizes structured JSON data.

## 🛠️ Tech Stack
- **Language:** Python 3.13+
- **Model:** Gemini 2.5 Flash (via `google-genai` SDK)
- **Environment Management:** `python-dotenv`
- **Version Control:** Git

## 🧪 Phase 1:Core Techniques Implemented
I implemented five critical strategies to control and optimize LLM outputs:
### 1. Zero-shot Prompting
Sending a direct instruction without previous examples. Used here to summarize complex technical topics for non-technical audiences.

### 2. Few-shot Prompting
Providing the model with a small set of "shots" (examples) to establish pattern recognition. Demonstrated through a sentiment analysis task.

### 3. Chain-of-Thought (CoT)
Forcing the model to output its internal reasoning steps before providing a final answer. This significantly improves accuracy in logical and mathematical problem-solving.

### 4. System Instructions
Defining a permanent "persona" or "behavioral guardrails" for the model. Implemented by setting a **Senior Backend Engineer** persona that prioritizes time/space complexity analysis.

### 5. JSON Output Mode
The most critical developer technique. Using `response_mime_type="application/json"` to force the model to return machine-readable data, allowing for seamless integration into databases and APIs.

## 🧪 Phase 2:Professional Email Drafter CLI
A functional command-line utility located in the `/email_drafter` folder that automates professional correspondence.
**Key Features:**
1. **Structured Data:** Forces Gemini to separate the `subject` and `body` into a JSON object.
2. **Dynamic Inputs**: Uses argparse to handle `--situation`, `--tone`, and `--save` flags.
3. **Safe Storage:** Automatically archives every draft in an `/outputs` folder with unique timestamps.

## How to Run:
```bash
   cd email_drafter
   python drafter.py --situation "Applying for a project intern role at Google" --tone "ambitious" --save google_app
```
## 🚀 Getting Started

### Prerequisites
1. Obtain a free API Key from [Google AI Studio](https://aistudio.google.com/).
2. Install dependencies:
   ```bash
   pip install google-genai python-dotenv

### Installation
1. **Clone the repo:**`git clone https://github.com/vivekraj02/Gemini-Prompt-Engineering.git`
2. **Setup .env:**Add `GEMINI_API_KEY=your_key` to a `.env` file in the root.
