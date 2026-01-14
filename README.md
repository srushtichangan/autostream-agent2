# AutoStream AI Sales Agent

## 1. How to Run the Project

## How to Run Locally
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Set OPENAI_API_KEY
4. Run:
   python main.py

## 2. Architecture Explanation

This project implements a conversational AI sales agent for AutoStream using Python. 
The system is divided into modular components to simulate a real-world agentic workflow.

Intent detection is handled in a separate module, where user inputs are classified into 
greeting, pricing inquiry, or high-intent lead. This allows the agent to respond 
appropriately at each stage of the conversation.

A Retrieval-Augmented Generation (RAG) approach is used with a local JSON knowledge base 
containing pricing and policy information. This ensures that responses are accurate, 
controlled, and do not rely on hard-coded text.

State management is handled using an in-memory dictionary that stores user details 
(name, email, platform) across multiple conversation turns. This ensures that the lead 
capture tool is only triggered after all required information is collected.

Finally, a mock lead capture tool simulates backend integration by printing captured 
lead details. This design mirrors real-world SaaS sales automation workflows.

---

## 3. WhatsApp Deployment Using Webhooks

This agent can be integrated with WhatsApp using webhook-based communication. 
Incoming messages from WhatsApp (via Twilio or Meta WhatsApp Cloud API) would be sent 
to a backend server where the agent logic runs. The agent processes the message, 
updates conversation state, and sends a response back through the WhatsApp API. 
User state can be stored in a database like Redis to support multi-turn conversations.

