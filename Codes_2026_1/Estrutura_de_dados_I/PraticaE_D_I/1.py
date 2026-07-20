def calculate_factorial(n):
    """Calculates N! manually."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def generate_permutations(elements):
    """Generates all possible routes manually via recursion."""
    if len(elements) <= 1:
        yield elements
        return
    
    for i in range(len(elements)):
        current_city = elements[i]
        remaining_cities = elements[:i] + elements[i+1:]
        
        for path in generate_permutations(remaining_cities):
            yield [current_city] + path

def demonstrate_tsp_explosion():
    print(f"{'Cities (N)':<12} | {'Expected Routes (N!)':<22} | {'Routes Actually Calculated'}")
    print("-" * 65)

    n = 3
    # Infinite loop: runs until manually stopped or system crash
    while True:
        cities = list(range(n))
        
        route_count = 0
        for _ in generate_permutations(cities):
            route_count += 1
            
        expected_routes = calculate_factorial(n)
        
        print(f"{n:<12} | {expected_routes:<22} | {route_count}")
        
        n += 1

# Execute the code
demonstrate_tsp_explosion()