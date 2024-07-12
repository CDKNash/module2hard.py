import random
core1 = random.randint(3, 20)
print(core1)
parol = ""
for core2 in range(1, 20):
    for core3 in range(core2 + 1, 20):
        if core1 % (core2 + core3) == 0:
            parol += str(core2) + str(core3)
print(parol)
