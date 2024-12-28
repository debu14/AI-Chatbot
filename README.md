# AI-Chatbot

This project demonstrates a chatbot implementation using OpenAI's GPT model with LangChain's `ConversationChain`. The bot leverages a `ConversationBufferMemory` to maintain the context of the conversation, allowing for more dynamic and interactive dialogues.

## Features
- Conversational AI powered by OpenAI's GPT model.
- Contextual memory of the chat using LangChain's `ConversationBufferMemory`.
- Easy integration with environment variables for secure API key management.
- Adjustable creativity level via the `temperature` parameter.

## Prerequisites

Before running the project, ensure you have the following installed:

1. Python 3.8+
2. Required Python libraries (specified in the `requirements.txt` file).
3. OpenAI API key.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/debu14/AI-Chatbot
   cd AI-Chatbot

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt

##  Usage
Create a .env file in the root of the project and add your OpenAI API key:
```bash
   OPENAI_API_KEY=your_openai_api_key
```
Run the Chatbot
```bash
   python chatbot.py
```

