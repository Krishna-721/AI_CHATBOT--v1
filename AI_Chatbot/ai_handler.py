# ai_handler.py
import os
import openai
import google.generativeai as genai
# import anthropic

# Load API keys (multiple keys separated by commas)
OPENAI_KEYS = os.getenv("OPENAI_API_KEY", "").split(",")
# CLAUDE_KEY = os.getenv("CLAUDE_KEY", "")
GEMINI_KEY = os.getenv("GEMINI_KEY", "")

# Setup Gemini
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)

# Setup Claude (commented out for now)
# claude_client = anthropic.Anthropic(api_key=CLAUDE_KEY) if CLAUDE_KEY else None

# Initialize key index
current_openai_key_index = 0

def get_openai_response(prompt):
    global current_openai_key_index
    for _ in range(len(OPENAI_KEYS)):
        try:
            openai.api_key = OPENAI_KEYS[current_openai_key_index].strip()
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message["content"]
        except Exception as e:
            if "quota" in str(e).lower() or "limit" in str(e).lower():
                current_openai_key_index = (current_openai_key_index + 1) % len(OPENAI_KEYS)
            else:
                raise
    raise Exception("All OpenAI keys exhausted.")

def get_gemini_response(prompt):
    if not GEMINI_KEY:
        raise Exception("Gemini API key not set.")
    model = genai.GenerativeModel("gemini-1.5-pro")
    resp = model.generate_content(prompt)
    return resp.text

def get_ai_response(prompt):
    try:
        return get_openai_response(prompt)
    except Exception as e:
        print(f"OpenAI failed: {e}")
    try:
        return get_gemini_response(prompt)
    except Exception as e:
        print(f"Gemini failed: {e}")
    return "All AI services are currently unavailable."
