from litellm import completion

# Select and change model
model_name = "gemini/gemini-2.5-flash"

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

    # Add refinement instruction
    conversation.append({
        "role": "user",
        "content": question
    })

    # Call LiteLLM
    response = completion(
        model=model_name,
        messages=conversation
    )

    # Extract assistant response
    ai_message = response["choices"][0]["message"]["content"]

    print(f"\n--- Step {step} ---\n")
    print(ai_message)

    # Save assistant response into history
    conversation.append({
        "role": "assistant",
        "content": ai_message
    })

print("\nSequence completed.")
