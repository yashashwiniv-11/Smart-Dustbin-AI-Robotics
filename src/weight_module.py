import random
weight = 0  

def check_weight():
    global weight  
    weight += random.randint(1, 5)

    print("Current Weight:", weight, "kg")

    if weight >= 15:
        print("Status: BIN FULL")
        weight = 0 
        return weight, "FULL"
    else:
        print("Status: NOT FULL")
        return weight, "NOT FULL"# Force update commit
# Force update commit
