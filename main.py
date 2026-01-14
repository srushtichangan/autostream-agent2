from agent.intent import detect_intent
from agent.rag import get_pricing_response
from agent.state import init_state
from agent.tools import mock_lead_capture

def main():
    print("🚀 AutoStream Agent Running\n")

    state = init_state()

    while True:
        user_input = input("User: ")

        intent = detect_intent(user_input)
        state["intent"] = intent

        # Greeting
        if intent == "greeting":
            print("Agent: Hi! How can I help you today?")

        # Pricing inquiry
        elif intent == "pricing":
            print("Agent:", get_pricing_response())

        # High intent flow
        elif intent == "high_intent":
            print("Agent: Great! Let me get you started.")

            if not state["name"]:
                state["name"] = input("Agent: What's your name? ")

            if not state["email"]:
                state["email"] = input("Agent: Your email address? ")

            if not state["platform"]:
                state["platform"] = input(
                    "Agent: Which platform do you create content on? "
                )

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
            break

if __name__ == "__main__":
    main()
