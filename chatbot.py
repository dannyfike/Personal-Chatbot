import requests

# 🔑 Put your OpenRouter API key here
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def chat_with_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "deepseek/deepseek-r1:free",  # free model for testing
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post(BASE_URL, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("🤖 Jarvis Online. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Jarvis: Goodbye, sir.")
            break
        reply = chat_with_ai(user_input)
        print("Jarvis:", reply)
