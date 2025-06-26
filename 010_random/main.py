import random

# Random integers
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random float between 0 and 1
probability = random.random()
print(f"Random probability: {probability:.4f}")

# Random choice from list
colors = ['red', 'green', 'blue', 'yellow']
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# Random sample (multiple choices without replacement)
sample = random.sample(colors, 2)
print(f"Random sample: {sample}")
