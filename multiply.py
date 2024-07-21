multipliers = None
multipliers_map = None
multiplier = None

def initialise_multipliers():
    global multipliers
    global multipliers_map
    global multiplier

    multipliers = (1, 2, 4, 5, 6)
    multipliers_map = {
        1: 0.25,
        2: 0.5,
        4: 0.75,
        5: 1.5,
        6: 1.25
    }
    multiplier = 1
