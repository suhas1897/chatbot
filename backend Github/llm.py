import requests
import logging
import json
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"

try:
    response = requests.post(OLLAMA_API_URL, json={"model": MODEL_NAME, "prompt": "Test"})
    if response.status_code == 200:
        logger.info(f"Ollama {MODEL_NAME} initialized successfully")
        llm = True
    else:
        raise Exception(f"Ollama server responded with status {response.status_code}")
except Exception as e:
    logger.error(f"Error initializing Ollama: {e}")
    llm = None

def generate_response(prompt, context):
    if not llm:
        logger.error("LLM not initialized. Please check Ollama setup.")
        return "LLM not initialized. Please check Ollama setup."

    if context.get("action") == "book_appointment":
        prompt = (
            f"You are a medical chatbot assisting with appointment booking. "
            f"Respond naturally to '{prompt}' and guide the user to provide their name, date, time, and address. "
            f"Do not mention controlled substances or restrictions."
        )
    elif context.get("action") == "order_medicine":
        prompt = (
            f"You are a medical chatbot assisting with ordering common, non-controlled medications (e.g., Paracetamol, Ibuprofen). "
            f"Respond naturally to '{prompt}' and guide the user to list medicines and quantities (e.g., 'Paracetamol 10, Ibuprofen 5'), "
            f"then provide their name and address. Do not mention controlled substances or restrictions."
        )
    else:
        prompt = (
            f"You are a medical chatbot providing general health information. "
            f"Respond to the query '{prompt}' with accurate, helpful information about common medical topics. "
            f"Do not mention controlled substances or restrictions unless explicitly relevant."
        )

    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 200
            }
        }
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response from LLM").strip()
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return f"Error generating response: {str(e)}"