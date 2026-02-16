from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Select and change model
model_options = {
    "1": "gemini/gemini-2.5-flash",
    "2": "claude-3-5-sonnet-20240620",
    "3": "gpt-4o-mini"
}

choice = input("Choose model (1/2/3): ").strip()
if choice not in model_options:
    raise ValueError("Invalid model choice (must be 1/2/3)")

model_name = model_options[choice]

# Define api_key BEFORE calling completion()
if model_name.startswith("gemini"):
    api_key = os.getenv("GEMINI_API_KEY")
elif model_name.startswith("claude"):
    api_key = os.getenv("ANTHROPIC_API_KEY")
elif model_name.startswith("gpt"):
    api_key = os.getenv("OPENAI_API_KEY")
else:
    raise ValueError("Unsupported model")

if not api_key:
    raise RuntimeError(f"API key not found for selected model: {model_name}")

# Fixed topic
topic = "Build a two-week campus visiting plan for famous universities in the United States."

# Predefined sequence of refinement questions
questions = [
    "First, create a general 2-week plan outline.",
    "Now optimize the plan for budget under $2000.",
    "Now prioritize top-ranked CS departments.",
    "Now improve the travel efficiency between cities.",
    "Finally, present a clean structured final version."
]

# Initialize conversation with system role
conversation = [
    {
        "role": "system",
        "content": (
            "You are a structured planner. "
            "Each new instruction modifies the previous answer. "
            "Do NOT restart from scratch."
        )
    },
    {
        "role": "user",
        "content": topic
    }
]

print("\nStarting automated sequence...\n")

for step, question in enumerate(questions, 1):

    conversation.append({
        "role": "user",
        "content": question
    })

    response = completion(
        model=model_name,
        messages=conversation,
        api_key=api_key
    )

    ai_message = response["choices"][0]["message"]["content"]

    print(f"\n--- Step {step} ---\n")
    print(ai_message)

    conversation.append({
        "role": "assistant",
        "content": ai_message
    })

print("\nSequence completed.")
