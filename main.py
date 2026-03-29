import requests
import time

TELEGRAM_TOKEN = "8787967605:AAGTA8NlxbPSR2jHh8ONVz7ZvnByuRmKU6I"
CHAT_ID = "8172803404"

API_URL = "https://www.apollorejser.dk/api/search"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def get_price():
    try:
        payload = {
            "destination": "Fuerteventura",
            "hotel": "Playitas Resort",
            "departureDate": "2026-05-19",
            "returnDate": "2026-05-26",
            "adults": 2,
            "children": [
                {"age": 5},
                {"age": 9},
                {"age": 11}
            ]
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json"
        }

        r = requests.post(API_URL, json=payload, headers=headers)

        data = r.json()

        # 🔥 Find pris i response
        prices = []

        if "results" in data:
            for item in data["results"]:
                if "price" in item:
                    prices.append(item["price"])

        if not prices:
            return "Ingen pris fundet"

        best_price = min(prices)

        return f"{best_price:,}".replace(",", ".") + " kr"

    except Exception as e:
        return f"Fejl: {e}"


last_price = None

while True:
    price = get_price()

    if price != last_price:
        send(f"✈️ Playitas (PRÆCIS)\n{price}")
        last_price = price

    time.sleep(86400)
