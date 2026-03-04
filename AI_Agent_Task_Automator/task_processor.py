def simple_ai_agent(text):
    print("\n--- AI Agent is processing your task ---")
    
    
    summary = text[:50] + "..." if len(text) > 50 else text
    
    
    words = text.split()
    keywords = [word for word in words if len(word) > 5]
    
    print(f"Summary: {summary}")
    print(f"Keywords found: {keywords[:3]}")
    print("--- Task Completed ---\n")

if __name__ == "__main__":
    user_input = input("Enter some text for the AI Agent to analyze: ")
    simple_ai_agent(user_input)