import random
import time
import json


def generate_ecu_data():

    ecu_data = {
        "rpm": random.randint(700, 5000),
        "temperature": random.randint(70, 120),
        "voltage": round(random.uniform(11.0, 14.5), 2)
    }

    return ecu_data


if __name__ == "__main__":

    while True:

        data = generate_ecu_data()

        print(data)

        # SAVE DATA
        with open("logs/live_ecu_data.json", "w") as file:
            json.dump(data, file)

        time.sleep(2)