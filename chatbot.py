import os
import openai
from langchain.chains.conversation.base import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from .env
openai.api_key  = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Add it to the .env file.")

# Initialize the chat model with OpenAI GPT
chat_model = ChatOpenAI(
    openai_api_key=openai.api_key,
    temperature=0.7  # Adjust temperature for more/less creative responses
)

# Memory for the conversation (stores chat history)
memory = ConversationBufferMemory()

# Conversation Chain
conversation = ConversationChain(
    llm=chat_model,
    memory=memory
)

def chat_with_bot():
    print("AI Chatbot (Type 'exit' to end the chat)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break
        response = conversation.run(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat_with_bot()