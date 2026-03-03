from sensor import Sensor
from dustbin import Dustbin
from utils import display_status
import random
import time

print("=== Smart Dustbin Management System Initialized ===")

sensor = Sensor()
dustbin = Dustbin(capacity=5)

while True:
    waste_type = sensor.detect_waste()
    weight = random.randint(1, 2)

    dustbin.add_waste(weight)

    display_status(waste_type, dustbin.current_weight, dustbin.status())

    if dustbin.is_full():
        print("\n⚠ ALERT: Maximum Capacity Reached.")
        print("Please empty the dustbin before continuing operation.")
        break

    time.sleep(2)
