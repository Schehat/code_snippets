import random

print(f"random number between 0 - 1 (exclusive): {random.random()}\n")

print(f"random float between 1 - 10: {random.uniform(1, 10)}\n")

print(f"random int between 1 - 6: {random.randint(1, 7)}\n")

print(f"random value in list: {random.choice(['red', 'green', 'blue'])}\n")

print(
    f"random values in list k-times: {random.choices(['red', 'green', 'blue'], k=10)}\n"
)

choices = random.choices(["red", "green", "blue"], weights=[18, 2, 18], k=10)
print(f"random values in list k-times: {choices}\n")

deck = list(range(1, 53))
random.shuffle(deck)  # inplace
print(f"shuffled deck: {deck}\n")

# sample wont pick an element multiple times in contrast to choices
hand = random.sample(deck, k=5)
print(f"sample hand: {hand}")
