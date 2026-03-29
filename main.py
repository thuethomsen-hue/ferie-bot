import requests
import time

TELEGRAM_TOKEN = "8787967605:AAGTA8NlxbPSR2jHh8ONVz7ZvnByuRmKU6I"
CHAT_ID = "8172803404"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def get_price():
    try:
        r = requests.get("https://www.apollorejser.dk/spanien/fuerteventura/playitas-resort")
        text = r.text

        if "kr" in text:
            return text.split("kr")[0][-10:] + " kr"
        return "Pris ikke fundet"
    except:
        return "Fejl"

while True:
    price = get_price()
    send(f"Pris: {price}")
    time.sleep(86400)
