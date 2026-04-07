import os
from langchain_groq import ChatGroq

# ✅ Import correct message types from langchain_core.messages
from langchain_core.messages import HumanMessage, SystemMessage

# Optionally set your Groq API key in code
# os.environ["GROQ_API_KEY"] = "your_api_key_here"

# Initialize the Groq chat model
chat_model = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.7,  # Creative pirate speech
    max_tokens=500,
)

# System message telling the model to be a pirate
system_message = SystemMessage(
    content=(
        "You are a friendly pirate who loves to share knowledge. "
        "Always respond in pirate speech, use pirate slang, and include lots of nautical references and emojis. ☠️🏴‍☠️"
    )
)

# The question we want answered
question = "What are the 7 wonders of the world?"

# Build the chat messages list
messages = [
    system_message,
    HumanMessage(content=question),
]

# Invoke the model
response = chat_model.invoke(messages)

# Show the result
print("\nQuestion:", question)
print("\nPirate Response:")
print(response.content)