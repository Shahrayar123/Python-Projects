import openai

openai.api_key = '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' # Set your OpenAI API key

def ask_gpt3(prompt):
    response = openai.Completion.create(
        engine="YOUR GPT MODEL GOES HERE",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main loop for chatting with the GPT-3 powered chatbot
print("Welcome to the GPT-3 powered chatbot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    else:
        response = ask_gpt3(user_input)
        print("Chatbot:", response)
