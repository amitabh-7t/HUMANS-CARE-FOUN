def chatbot():
    print("Hello! I am a simple chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "your name" in user_input:
            print("Chatbot: I am a chatbot created to assist you.")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm here to help you!")
        elif "weather" in user_input:
            print("Chatbot: I don't have real-time weather information, but you can check online!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")

chatbot()
