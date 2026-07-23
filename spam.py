import requests
import time
import random
import string

while True:
    name = ''.join(random.choices(string.ascii_letters, k=8))

    requests.post(
        "http://127.0.0.1:5000/spam",
        data={
            "message": name
        }
    )

    print("Sent:", name)
    time.sleep(1)
