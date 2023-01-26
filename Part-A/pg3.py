# Initializing responses dictionary
responses = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you!",
    "what's your name?": "I am a chatbot, you can call me Bot.",
    "what do you do?": "I help people with their questions and queries.",
    "can you help me with something?": "Sure, what do you need help with?",
    "bye": "Goodbye!",
    "thank you": "You're welcome!",
    "what is your favourite colour?": "I am a computer program, I do not have a favourite colour.",
    "what is your favourite food?": "I am a computer program, I do not have a favourite food."
}

# default response
default = "I am sorry, I didn't understand what you said. Can you please rephrase your question?"

while True:
    user_input = input("You: ")
    if user_input.lower() in responses:
        print("Bot: ", responses[user_input])
    else:
        print("Bot: ", default)
