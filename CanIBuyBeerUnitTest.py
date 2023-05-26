def canIBuyBeer(age,location,promilleHalt):
    if promilleHalt > 1.0:
        return False
    if location == "S" and age < 19:
        return False
    if location == "K" and age < 18:
        return False
    return True

