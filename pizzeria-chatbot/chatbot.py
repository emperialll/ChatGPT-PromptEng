from context import CONTEXT
from llm_client import get_completion_from_messages


def message_collection(message):
    CONTEXT.append(message)
    return CONTEXT

def user_prompt():
    user_input = input("Customer: ")
    return user_input

def main():
    print("Welcome to King Pizzeria\n")
    while True:
        user_request = user_prompt()
        if user_request == "bye":
            break
        user_message = {'role':'user', 'content': user_request}
        messages = message_collection(user_message)
        
        bot_response = get_completion_from_messages(messages)
        bot_message = {'role':'system', 'content': bot_response}
        messages = message_collection(bot_message)
        
        print(f"Pizza Bot: {bot_response}")

if __name__ == "__main__":
    main()
