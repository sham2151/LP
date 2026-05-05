def chatbot():
    print("🤖 Customer Support Chatbot")
    print("Type 'exit' to quit\n")

    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! What can I do for you?",
        "order": "Please provide your order ID.",
        "refund": "Refunds are processed within 5-7 days.",
        "delivery": "Delivery takes 3-5 business days.",
        "payment": "We accept cards, UPI, and net banking.",
        "account": "Please check your account settings or reset your password.",
        "help": "I can help with orders, refunds, delivery, and payments."
    }

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Thank you! Goodbye 😊")
            break

        found = False
        for key in responses:
            if key in user:
                print("Bot:", responses[key])
                found = True
                break

        if not found:
            print("Bot: Sorry, I didn’t understand. Please try again.")


# Run chatbot
chatbot()