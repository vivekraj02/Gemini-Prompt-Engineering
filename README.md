# Gemini-Prompt-Engineering

# Gemini Prompt Engineering Essentials 🚀

A structured practice repository focused on mastering LLM implementation using the **Google Gemini 2.5 Flash** model. This project demonstrates the core technical strategies required to transition from a "chatbot user" to an "AI Prompt Engineer."

## 📌 Project Overview
This repository contains a comprehensive Python implementation of the 5 fundamental prompt engineering techniques. It serves as a foundational bridge to building production-ready AI applications, such as CLI tools and automated agents.

## 🛠️ Tech Stack
- **Language:** Python 3.13+
- **Model:** Gemini 2.5 Flash (via `google-genai` SDK)
- **Environment Management:** `python-dotenv`
- **Version Control:** Git

## 🧪 Core Techniques Implemented

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

## 🚀 Getting Started

### Prerequisites
1. Obtain a free API Key from [Google AI Studio](https://aistudio.google.com/).
2. Install dependencies:
   ```bash
   pip install google-genai python-dotenv
