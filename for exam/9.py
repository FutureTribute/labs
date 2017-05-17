import random

t = random.randint(5, 20)
# print(t)
for i in range(9, 21):
    t -= random.randint(1, 5)
    # print(t)
    if t < 0:
        break
print("Hour:", i)
