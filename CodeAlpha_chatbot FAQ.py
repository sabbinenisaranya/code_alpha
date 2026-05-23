def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("Chatbot: Hi there!")

        elif "how are you" in user:
            print("Chatbot: I'm fine, thanks! How about you?")

        elif "bye" in user:
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: I'm sorry, I don't understand the question.")


chatbot()