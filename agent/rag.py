import json

def load_knowledge():
    return {
        "pricing": {
            "basic": {
                "price": "$29/month",
                "videos": "10 videos/month",
                "resolution": "720p"
            },
            "pro": {
                "price": "$79/month",
                "videos": "Unlimited videos",
                "resolution": "4K",
                "features": "AI captions"
            }
        },
        "policies": {
            "refund": "No refunds after 7 days",
            "support": "24/7 support available only on Pro plan"
        }
    }

def get_pricing_response():
    data = load_knowledge()
    basic = data["pricing"]["basic"]
    pro = data["pricing"]["pro"]

    return (
        "AutoStream offers two plans:\n"
        f"1) Basic Plan: {basic['price']}, {basic['videos']}, {basic['resolution']} resolution\n"
        f"2) Pro Plan: {pro['price']}, {pro['videos']}, "
        f"{pro['resolution']} resolution, {pro['features']}"
    )



