
import os
import requests
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

SYSTEM_PROMPT = (
    "Kamu adalah asisten chatbot berbahasa Indonesia. Jawab sopan, singkat, dan jelas. "
    "Jika pertanyaan kurang lengkap, minta klarifikasi singkat."
)

def respond(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user, assistant in history:
        if user:
            messages.append({"role": "user", "content": user})
        if assistant:
            messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": message})

    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "options": {"temperature": 0.3},
        "stream": False,
    }
    try:
        r = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload, timeout=120)
        r.raise_for_status()
        data = r.json()
        return data.get("message", {}).get("content", "(tidak ada respons dari model)")
    except Exception as e:
        return f"Terjadi error panggilan ke Ollama: {e}\nPastikan Ollama berjalan dan model '{OLLAMA_MODEL}' sudah di-pull."

demo = gr.ChatInterface(
    fn=respond,
    title="Hacktiv8 Chatbot (Offline via Ollama)",
    description="Chatbot lokal/offline memakai model dari Ollama. Jalankan Ollama & pull model terlebih dulu."
)

if __name__ == "__main__":
    demo.launch()
