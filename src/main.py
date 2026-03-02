import random
import time

class SmartDustbin:

    def __init__(self):
        self.weight = 0
        self.cycle_count = 0
        self.full_count = 0
        self.waste_stats = {
            "Dry": 0,
            "Wet": 0,
            "Plastic": 0,
            "Metal": 0
        }

    def detect_waste(self):
        waste_types = ["Dry", "Wet", "Plastic", "Metal"]
        detected = random.choice(waste_types)
        print("Detected Waste Type:", detected)
        self.waste_stats[detected] += 1

    def check_weight(self):
        self.weight += random.randint(1, 5)
        print("Current Weight:", self.weight, "kg")

        if self.weight >= 15:
            print("Status: BIN FULL")
            self.full_count += 1
            self.weight = 0
            return True
        else:
            print("Status: NOT FULL")
            return False

    def move_to_dump(self):
        print("Initiating autonomous movement from Source Point...")
        print("Navigating along predefined LED path...")
        print("Reached Destination: Main Dump Station")
        print("Executing waste unloading into categorized compartments...")
        print("Returning back to Source Point...")

    def run(self):
        print("Smart Dustbin System Activated")
        print("--------------------------------")

        while True:
            self.cycle_count += 1

            self.detect_waste()

            if self.check_weight():
                self.move_to_dump()
                print("Waste disposal process completed successfully.")
                break

            print("System is monitoring for the next waste input...")
            time.sleep(2)

        print("\n----- SYSTEM SUMMARY -----")
        print("Total Monitoring Cycles:", self.cycle_count)
        print("Total Times Bin Was Full:", self.full_count)
        print("Waste Distribution:")
        for key, value in self.waste_stats.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    dustbin = SmartDustbin()
    dustbin.run()