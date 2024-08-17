multipliers = None
multipliers_map = None
multiplier = None
penalties = None
still_rounds = None

#it stands for multipliers && penalties
def initialise_multipliers():
    global multipliers
    global multipliers_map
    global multiplier
    global penalties
    global still_rounds

    multipliers = (1, 2, 4, 5, 6)
    multipliers_map = {
        1: 0.5,
        2: 0.3,
        4: 0.2,
        5: 2.5,
        6: 3.08
    }
    multiplier = 1
    penalties = (11,12,13,14,15)
    still_rounds = 0