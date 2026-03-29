import requests
import time
import re

TELEGRAM_TOKEN = "8787967605:AAGTA8NlxbPSR2jHh8ONVz7ZvnByuRmKU6I"
CHAT_ID = "8172803404"

URL = "https://www.apollorejser.dk/spanien/fuerteventura/playitas-resort"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def get_price():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(URL, headers=headers)
        text = r.text

        # Find alle priser
        prices = re.findall(r"\d{1,3}(?:\.\d{3})+ ?kr", text)

        # Filtrer realistiske feriepriser
        cleaned = []
        for p in prices:
            number = int(p.replace(".", "").replace("kr", "").strip())
            if 3000 < number < 50000:
                cleaned.append(number)

        if not cleaned:
            return "Ingen pris fundet"

        # Tag laveste pris
        best_price = min(cleaned)

        return f"{best_price:,}".replace(",", ".") + " kr"

    except Exception as e:
        return f"Fejl: {e}"


# husk sidste pris
last_price = None

while True:
    price = get_price()

    if price != last_price:
        send(f"✈️ Playitas pris:\n{price}")
        last_price = price

    time.sleep(86400)
