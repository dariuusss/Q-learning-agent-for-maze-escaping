multipliers = None
multipliers_map = None
multiplier = None

def initialise_multipliers():
    global multipliers
    global multipliers_map
    global multiplier

    multipliers = (1, 2, 4, 5, 6)
    multipliers_map = {
        1: 0.5,
        2: 0.3,
        4: 0.2,
        5: 2.5,
        6: 3.08
    }
    multiplier = 1
