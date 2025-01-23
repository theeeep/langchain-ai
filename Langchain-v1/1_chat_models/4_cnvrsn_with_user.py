from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0.0, max_tokens=2000)

chat_history = []  # Initialize an empty chat history list of storage messages

# Set Initial System Message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")

# Add the system message to the chat history
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(
        HumanMessage(content=query)
    )  # Add the user's message to the chat history

    # Generate the AI's response
    # response = model.predict(chat_history)
    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(
        AIMessage(content=response)
    )  # Add the AI's response to the chat history

    print(f"AI: {response}")

print("____ Message History ____")
print(chat_history)
