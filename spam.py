import requests
import time

while True:
    response = requests.post(
        "http://127.0.0.1:5000/spam",
        data={"message": "Hello from Python"}
    )

    print(response.status_code)
    time.sleep(1)
