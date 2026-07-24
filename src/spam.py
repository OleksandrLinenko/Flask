import requests
import random
import time

while True:
    sensor = random.choice(["fall", "impact"])

    if sensor == "fall":
        data = {
            "sensor": "fall",
            "detected": random.choice([True, False]),
            "strength": random.randint(1, 10)
        }

    else:
        data = {
            "sensor": "impact",
            "force": round(random.uniform(5.0, 50.0), 1),
            "unit": "N"
        }

    response = requests.post(
        "http://127.0.0.1:5000/spam",
        json=data
    )

    print(response.status_code, data)

    time.sleep(1)
