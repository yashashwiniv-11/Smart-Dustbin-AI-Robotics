import random
class Sensor:
    def detect_waste(self):
        waste_types = ["Wet", "Dry", "Metal"]
        detected = random.choice(waste_types)
        return detected
