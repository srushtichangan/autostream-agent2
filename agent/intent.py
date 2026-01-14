def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in ["buy", "try", "sign up", "subscribe", "pro plan"]):
        return "high_intent"

    if any(word in text for word in ["price", "pricing", "plan", "plans"]):
        return "pricing"

    return "greeting"


