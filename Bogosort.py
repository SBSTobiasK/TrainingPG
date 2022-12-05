import copy
import random

x=0
deck1 = [x + 1 for x in range(12)]
deck2 = copy.deepcopy(deck1)
#random.seed(4)
random.shuffle(deck2)

while True:
    x += 1
    random.shuffle(deck2)
    if deck1 == deck2:
        print("Nach", x, "Versuchen waren die Karten wieder in der richtigen Reihenfolge")
        break

