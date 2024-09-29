import random
from main import Weighted, fruits

def calculate_manual_weight_value(chromosomes, fruit_weights, fruit_values):
    """Helper function to calculate total weight and value manually."""
    total_weight = sum(fruit_weights[i] for i, c in enumerate(chromosomes) if c)
    total_value = sum(fruit_values[i] for i, c in enumerate(chromosomes) if c)
    return total_weight, total_value

def test_fruit_knapsack():
    # Extract weights and values
    fruit_weights = [fruit["weight"] for fruit in fruits]
    fruit_values = [fruit["value"] for fruit in fruits]

    # Test Case 1: Standard random selection
    print("Running Test Case 1: Standard Random Selection")
    chromosomes = [random.choice([True, False]) for _ in fruit_weights]
    print(f"Test Case 1 Chromosome: {chromosomes}")
    individual = Weighted(fruit_weights, fruit_values, chromosomes)
    manual_weight, manual_value = calculate_manual_weight_value(chromosomes, fruit_weights, fruit_values)

    if manual_weight > individual.max_weight:
        assert individual.total_weight == 0 and individual.total_value == 0, "Test Case 1 Failed! Expected weight and value to be reset to 0."
    else:
        assert individual.total_weight == manual_weight, "Test Case 1 Failed! Incorrect total weight."
        assert individual.total_value == manual_value, "Test Case 1 Failed! Incorrect total value."
    
    print(f"Test Case 1 Total Weight: {individual.total_weight}, Total Value: {individual.total_value}")
    print(f"Test Case 1 Passed!\n")

    # Test Case 2: Close to max weight (manually selected)
    print("Running Test Case 2: Close to Max Weight")
    # Use specific items that together stay within the limit but are close
    chromosomes = [True, True, False, True, True, False, False, False, True, False, True, False, False, True, True, False]
    print(f"Test Case 2 Chromosome: {chromosomes}")
    individual = Weighted(fruit_weights, fruit_values, chromosomes)
    manual_weight, manual_value = calculate_manual_weight_value(chromosomes, fruit_weights, fruit_values)

    if manual_weight > individual.max_weight:
        assert individual.total_weight == 0 and individual.total_value == 0, "Test Case 2 Failed! Expected weight and value to be reset to 0."
    else:
        assert individual.total_weight == manual_weight, "Test Case 2 Failed! Incorrect total weight."
        assert individual.total_value == manual_value, "Test Case 2 Failed! Incorrect total value."
    
    print(f"Test Case 2 Total Weight: {individual.total_weight}, Total Value: {individual.total_value}")
    print(f"Test Case 2 Passed!\n")

    # Test Case 3: No items selected
    print("Running Test Case 3: No Items Selected")
    chromosomes = [False for _ in fruit_weights]  # No item is selected
    individual = Weighted(fruit_weights, fruit_values, chromosomes)
    manual_weight, manual_value = calculate_manual_weight_value(chromosomes, fruit_weights, fruit_values)
    
    assert individual.total_weight == manual_weight, "Test Case 3 Failed! Incorrect total weight."
    assert individual.total_value == manual_value, "Test Case 3 Failed! Incorrect total value."
    
    print(f"Test Case 3 Total Weight: {individual.total_weight}, Total Value: {individual.total_value}")
    print(f"Test Case 3 Passed!\n")

    # Test Case 4: All items selected
    print("Running Test Case 4: All Items Selected")
    chromosomes = [True for _ in fruit_weights]  # All items are selected
    individual = Weighted(fruit_weights, fruit_values, chromosomes)
    manual_weight, manual_value = calculate_manual_weight_value(chromosomes, fruit_weights, fruit_values)
    
    if manual_weight > individual.max_weight:
        assert individual.total_weight == 0 and individual.total_value == 0, "Test Case 4 Failed! Expected weight and value to be reset to 0."
    else:
        assert individual.total_weight == manual_weight, "Test Case 4 Failed! Incorrect total weight."
        assert individual.total_value == manual_value, "Test Case 4 Failed! Incorrect total value."
    
    print(f"Test Case 4 Total Weight: {individual.total_weight}, Total Value: {individual.total_value}")
    print(f"Test Case 4 Passed!\n")

    # Test Case 5: High-value items selected (manually select valuable ones)
    print("Running Test Case 5: High-Value Items Selected")
    chromosomes = [True if fruit["value"] >= 90 else False for fruit in fruits]  # Select high-value items
    individual = Weighted(fruit_weights, fruit_values, chromosomes)
    manual_weight, manual_value = calculate_manual_weight_value(chromosomes, fruit_weights, fruit_values)
    
    if manual_weight > individual.max_weight:
        assert individual.total_weight == 0 and individual.total_value == 0, "Test Case 5 Failed! Expected weight and value to be reset to 0."
    else:
        assert individual.total_weight == manual_weight, "Test Case 5 Failed! Incorrect total weight."
        assert individual.total_value == manual_value, "Test Case 5 Failed! Incorrect total value."
    
    print(f"Test Case 5 Total Weight: {individual.total_weight}, Total Value: {individual.total_value}")
    print(f"Test Case 5 Passed!\n")

if __name__ == "__main__":
    test_fruit_knapsack()
