import random

lottozahlen = [i for i in range(1, 49+1)]

gezogene_zahlen = []

for _ in range(6):
    ziehung = lottozahlen[random.randint(0, len(lottozahlen)-1)]
    lottozahlen.remove(ziehung)
    gezogene_zahlen.append(ziehung)

gezogene_zahlen.sort()

print(lottozahlen)
print(gezogene_zahlen)
print(random.randint(0,9))