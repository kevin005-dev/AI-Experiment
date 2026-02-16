import os
from litellm import completion

#API Key
os.environ["GEMINI_API_KEY"] = "Your API Key"

response = completion(
    model="gemini/gemini-2.5-flash", 
    messages=[{"role": "user", "content": "How do I say 'Hello' in Spanish?"}]
)

print(response.choices[0].message.content)
