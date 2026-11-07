import time
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1568759108931158197/gkKjAfznJz6rD_Y8cZF-k2R_Q52XlKWL99xBSReY-c0JLB1OZmEB2ckZYVxxM35FUZHD"
MESSAGE = "tung tung tung sahur"

print("Webhook loop running...")

while True:
  try:
    res = requests.post(WEBHOOK_URL, json={"content": MESSAGE})
    if res.status_code == 204:
      print("Sent message!")
    else:
      print(f"Failed status code: {res.status_code}")
  except Exception as e:
    print(f"Error: {e}")

  time.sleep(60)
