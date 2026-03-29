import requests
import time
from playwright.sync_api import sync_playwright

TELEGRAM_TOKEN = 8787967605:AAGTA8NlxbPSR2jHh8ONVz7ZvnByuRmKU6I
CHAT_ID = "8172803404"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def get_price():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.apollorejser.dk/spanien/fuerteventura/playitas-resort")
        page.wait_for_timeout(8000)

        prices = page.locator("text=kr").all_text_contents()
        browser.close()

        return prices[0] if prices else "Ingen pris fundet"

while True:
    send(get_price())
    time.sleep(86400)
