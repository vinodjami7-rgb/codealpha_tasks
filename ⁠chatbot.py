def simple_chatbot():
    print("--- Welcome to CodeAlpha Chatbot! ---")
    print("Type your message below (or type 'bye' to exit):")

    while True:
        user_input = input("\nYou: ").strip().lower()

        # Rule-based logic checking for predefined keywords
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks! How about you?")
        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        elif user_input == "":
            print("Chatbot: I didn't catch that. Could you please type something?")
        else:
            print("Chatbot: I am a simple rule-based bot. I can handle greetings like 'hello', 'how are you', or 'bye'!")

if __name__ == "__main__":
    simple_chatbot()
