# Pizzeria Chatbot

This module is a simple terminal-based chatbot for collecting pizza restaurant orders.

It demonstrates how a system prompt can define an assistant's role, menu knowledge, conversation style, and ordering workflow.

---

## Goal

Build a lightweight conversational ordering assistant that can:

- Greet the customer
- Collect a pizza order
- Clarify sizes, toppings, extras, and drinks
- Ask whether the order is for pickup or delivery
- Collect a delivery address when needed
- Summarize the full order
- Ask whether the customer wants anything else
- Collect payment information
- Keep responses short, friendly, and conversational

---

## Project Structure

```text
pizzeria-chatbot/
├── README.md
├── chatbot.py
├── context.py
└── llm_client.py
```

---

## Files

| File            | Purpose                                                          |
| --------------- | ---------------------------------------------------------------- |
| `context.py`    | Stores the system prompt, menu, and conversation rules           |
| `chatbot.py`    | Runs the terminal chatbot loop and stores conversation messages  |
| `llm_client.py` | Creates the OpenAI client and sends message history to the model |

---

## How It Works

The chatbot starts with a system message in `context.py`. That message tells the model to act as `OrderBot`, an automated pizza restaurant ordering assistant.

The system prompt includes:

- The assistant role
- The desired conversation flow
- The response style
- The pizza menu
- Toppings
- Drinks
- Pickup and delivery behavior
- Payment collection behavior

`chatbot.py` then repeatedly:

1. Reads user input from the terminal
2. Adds the user message to the shared conversation context
3. Sends the full context to the model
4. Prints the bot response
5. Adds the bot response back into the conversation history
6. Stops when the user types `bye`

---

## Menu Covered by the Bot

The system prompt currently includes:

### Pizzas

- Pepperoni pizza — `12.95`, `10.00`, `7.00`
- Cheese pizza — `10.95`, `9.25`, `6.50`
- Eggplant pizza — `11.95`, `9.75`, `6.75`

### Sides

- Fries — `4.50`, `3.50`
- Greek salad — `7.25`

### Toppings

- Extra cheese — `2.00`
- Mushrooms — `1.50`
- Sausage — `3.00`
- Canadian bacon — `3.50`
- AI sauce — `1.50`
- Peppers — `1.00`

### Drinks

- Coke — `3.00`, `2.00`, `1.00`
- Sprite — `3.00`, `2.00`, `1.00`
- Bottled water — `5.00`

---

## How to Run

From the project root:

```bash
python pizzeria-chatbot/chatbot.py
```

Then chat with the bot in the terminal:

```text
Welcome to King Pizzeria

Customer: Hi
Pizza Bot: Hi there! Welcome to King Pizzeria. What would you like to order today?
Customer: I want a pepperoni pizza
Pizza Bot: Sure! What size pepperoni pizza would you like?
Customer: bye
```

Type `bye` to stop the chatbot.

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=your_preferred_model_here
```

`OPENAI_MODEL` is optional. Use a model available to your OpenAI account.

---

## Prompt Engineering Concepts Demonstrated

| Concept                     | How This Module Demonstrates It                            |
| --------------------------- | ---------------------------------------------------------- |
| System prompting            | Defines the bot's role, behavior, menu, and order flow     |
| Conversation memory         | Sends the accumulated message history with each turn       |
| Role-based assistant design | Makes the assistant behave like a restaurant order bot     |
| Clarifying questions        | Instructs the bot to clarify sizes, extras, and options    |
| Task completion flow        | Guides the user from greeting to order summary and payment |

---

## Key Takeaways

- A strong system prompt can shape a chatbot's behavior without complex application logic.
- Multi-turn context is essential for order-taking because each response depends on previous user choices.
- Menu and pricing information can be embedded directly in the prompt for a small prototype.
- The chatbot can be improved by separating conversation state from model-generated text.

---

## Possible Improvements

- Track the order in a structured Python object
- Generate a final receipt with itemized prices and total cost
- Validate menu items and prices outside the model
- Add named pizza and drink sizes to make the menu clearer
- Store bot replies with the `assistant` role in the message history
- Add error handling for missing API keys or failed model calls
- Add tests for common ordering flows
- Build a simple web UI with Flask, FastAPI, or Streamlit
