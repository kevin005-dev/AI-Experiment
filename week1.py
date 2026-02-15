from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment")

response = completion(
  model="gemini/gemini-2.5-flash",
  # model="claude-3-5-sonnet-20240620",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
  temperature=0.7
)

for chunk in response:
    print(chunk["choices"][0]["delta"].get("content", ""), end="", flush=True)
