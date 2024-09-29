import random
import matplotlib.pyplot as plt
import pandas as pd

# Fruit data: names, weights, and values
fruits = [
    {"name": "Apple", "weight": 150, "value": 60},
    {"name": "Banana", "weight": 100, "value": 30},
    {"name": "Orange", "weight": 120, "value": 50},
    {"name": "Watermelon", "weight": 200, "value": 100},
    {"name": "Kiwi", "weight": 80, "value": 40},
    {"name": "Pineapple", "weight": 220, "value": 120},
    {"name": "Grapes", "weight": 75, "value": 20},
    {"name": "Mango", "weight": 180, "value": 90},
    {"name": "Melon", "weight": 300, "value": 150},
    {"name": "Peach", "weight": 90, "value": 35},
    {"name": "Pear", "weight": 110, "value": 55},
    {"name": "Papaya", "weight": 160, "value": 80},
    {"name": "Plum", "weight": 140, "value": 45},
    {"name": "Strawberry", "weight": 130, "value": 25},
    {"name": "Blueberry", "weight": 210, "value": 70},
    {"name": "Avocado", "weight": 170, "value": 85},
]

# Extract weights and values
fruit_weights = [fruit["weight"] for fruit in fruits]
fruit_values = [fruit["value"] for fruit in fruits]

# Initialize parameters
population_count = 20  # Combinations to choose the best solution from
rounds = 30  # Evolutions count
chromosomes = [[random.choice([True, False]) for _ in fruit_weights] for _ in range(population_count)]

class Weighted:
    max_weight = 1300  # grams

    def __init__(self, fruit_weights, fruit_values, chromosome):
        self.chromosome = chromosome
        self.fruits_in_bag = [fruit_weights[i] for i, c in enumerate(chromosome) if c]
        self.total_weight = sum(self.fruits_in_bag)
        self.total_value = sum(fruit_values[i] for i, c in enumerate(chromosome) if c)

        # Diagnostic logging
        print(f"Chromosome: {chromosome}")
        print(f"Selected Weights: {self.fruits_in_bag}, Total Weight: {self.total_weight}")
        print(f"Selected Values: {self.total_value}")

        # Only reset to 0 if the total weight strictly exceeds max_weight
        if self.total_weight > self.max_weight:
            print(f"Total weight exceeds max allowed weight ({self.max_weight}g). Resetting values.")
            self.total_weight = 0
            self.total_value = 0  # Reset both weight and value if the weight exceeds the limit
        else:
            print("Weight is within the limit. No reset required.")

    def __lt__(self, other):
        return self.total_value < other.total_value  # Sort by total value



# Track best weights and values over rounds
best_weights = []
best_values = []

for r in range(rounds):
    print(f"=== ROUND {r}, population {len(chromosomes)} ===")
    weighted = [Weighted(fruit_weights, fruit_values, chromosome) for chromosome in chromosomes]

    # selection
    best = sorted(weighted, reverse=True)[:2]
    best_weights.append(best[0].total_weight)
    best_values.append(best[0].total_value)
    print(f"Best weight: {best[0].total_weight}, Best value: {best[0].total_value}")

    # crossover
    offspring = [b.chromosome for b in best]
    for i in range(int((population_count - 2) / 2)):
        split_index = random.randint(0, len(offspring) - 1)
        c1 = offspring[0][:split_index] + offspring[1][split_index:]
        c2 = offspring[1][:split_index] + offspring[0][split_index:]

        # mutation
        for i in range(len(c1)):
            if random.randint(0, 5) == 1:
                c1[i] = random.choice([True, False])
            if random.randint(0, 5) == 1:
                c2[i] = random.choice([True, False])

        offspring.append(c1)
        offspring.append(c2)

    chromosomes = offspring

print("\nBag contains:")
print(f"Total weight: {best[0].total_weight}")
print(f"Total value: {best[0].total_value}")
selected_fruits = [fruits[i]["name"] for i, c in enumerate(best[0].chromosome) if c]
print(f"Fruit selection: {selected_fruits}")

# Plot best weight and value over rounds
plt.figure(figsize=(10, 6))
plt.plot(range(rounds), best_weights, marker='o', label='Best Weight')
plt.plot(range(rounds), best_values, marker='s', label='Best Value')
plt.title('Best Weight and Value Over Generations')
plt.xlabel('Generation')
plt.ylabel('Best Weight / Value')
plt.legend()
plt.grid(True)
plt.show()

# Create a table with selected fruits
selected_fruit_data = [{"Fruit": fruits[i]["name"], "Weight (g)": fruits[i]["weight"], "Value ($)": fruits[i]["value"]}
                        for i, c in enumerate(best[0].chromosome) if c]
df = pd.DataFrame(selected_fruit_data)
print("\nSelected Fruits (Weights and Values):")
print(df)
