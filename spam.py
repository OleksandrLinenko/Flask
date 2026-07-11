import requests
import time

counter = 1

while True:
    response = requests.post(
        "http://127.0.0.1:5000/spam",
        data={
            "message": f"Message {counter}"
        }
    )

    print(response.status_code)
    counter += 1
    time.sleep(1)
