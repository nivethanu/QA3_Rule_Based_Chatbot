import re

def get_response(user_input):
    text = user_input.lower().strip()

    # Exit
    if text in ["bye", "exit", "quit"]:
        return "Thank you for using the Library Chatbot. Goodbye!"

    # Greeting
    if re.search(r"\b(hi|hello|hey)\b", text):
        return "Hello! How can I help you with library information?"

    # Library timings
    if re.search(r"\b(timing|hours|open)\b", text):
        return "The library is open from 9 AM to 5 PM, Monday to Friday."

    # Book issue
    if re.search(r"\b(issue|borrow book)\b", text):
        return "You can issue books using your library card at the counter."

    # Book return
    if re.search(r"\b(return book)\b", text):
        return "Books must be returned within 14 days to avoid fines."

    # Fine
    if re.search(r"\b(fine|penalty)\b", text):
        return "Fine is Rs.5 per day after the due date."

    # Default
    return "Sorry, I can help with timings, book issue, return, or fines."

def library_chatbot():
    print("LibraryBot: Welcome to the Library Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ")
        response = get_response(user)
        print("LibraryBot:", response)

        if user.lower() in ["bye", "exit", "quit"]:
            break

library_chatbot()
