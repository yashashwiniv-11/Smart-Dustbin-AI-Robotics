import random 

def detect_waste():
    waste_types = ["Dry", "Wet", "Plastic", "Metal"]
    detected = random.choice(waste_types)
    print("Detected Waste Type:", detected)
    return detected
