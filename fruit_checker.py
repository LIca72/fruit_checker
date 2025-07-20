# Fruit Checker Game — using sets in Python


fridge = {"apple", "banana", "kiwi", "pear"}


eaten_input = input("Which fruits did you eat? (e.g. apple, kiwi): ")


eaten = set(fruit.strip() for fruit in eaten_input.split(","))


eaten_real = fridge & eaten


left_in_fridge = fridge - eaten


imaginary = eaten - fridge

print("\n🍽️ You really ate (from the fridge):", eaten_real)
print("🧊 Still in the fridge:", left_in_fridge)
print("🌀 Not in the fridge (imagined):", imaginary)
