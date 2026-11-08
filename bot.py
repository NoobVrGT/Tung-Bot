import time
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1569034684892053630/QwGkcFuNWFLiN3kp2UcQ8I7wPRHQXhAarBSZOLzO2XeMaBZcJ_v_yJLkXxIJ4S754tc8"
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
