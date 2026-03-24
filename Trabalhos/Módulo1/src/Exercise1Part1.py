import math
import statistics

def multiples_of_six(a):
    upper_bound = a**2
    multiples = [x for x in range(a, upper_bound + 1) if x % 6 == 0]
    print(f"(a) Multiples of 6 between {a} and {upper_bound}: {multiples}")
    return multiples

def least_common_multiple(a, b):
    lcm_val = math.lcm(a, b)
    print(f"(b) LCM of {a} and {b} is: {lcm_val}")
    return lcm_val

def arithmetic_progression(N, u, r):
    terms = [u + i * r for i in range(N)]
    print(f"(c) Arithmetic Progression (N={N}, u={u}, r={r}): {terms}")
    return terms

def quadratic_roots(a, b, c):
    if a == 0:
        print(f"(d) Eq: {a}x^2 + {b}x + {c} = 0 -> Not a quadratic equation.")
        return None
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"(d) Eq: {a}x^2 + {b}x + {c} = 0 -> Real and distinct roots: {x1:.2f} and {x2:.2f}")
        return (x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        print(f"(d) Eq: {a}x^2 + {b}x + {c} = 0 -> Real double root: {x:.2f}")
        return (x,)
    else:
        print(f"(d) Eq: {a}x^2 + {b}x + {c} = 0 -> No real roots.")
        return ()

def vector_statistics(v):
    if not v:
        print("(e) Empty vector.")
        return None
    min_val = min(v)
    max_val = max(v)
    mean_val = statistics.mean(v)
    try:
        mode_val = statistics.mode(v)
    except statistics.StatisticsError:
        mode_val = "Multiple modes or no unique mode"
    
    print(f"(e) Vector {v} -> Min: {min_val}, Max: {max_val}, Mean: {mean_val:.2f}, Mode: {mode_val}")
    return min_val, max_val, mean_val, mode_val

def vector_intersection(v1, v2):
    intersection = list(set(v1) & set(v2))
    print(f"(f) Intersection of {v1} and {v2}: {intersection}")
    return intersection

def vector_union(v1, v2):
    union = list(set(v1) | set(v2))
    print(f"(g) Union of {v1} and {v2}: {union}")
    return union

if __name__ == "__main__":
    print("--- Tests for (a) ---")
    multiples_of_six(3)
    multiples_of_six(5)
    multiples_of_six(12)

    print("\n--- Tests for (b) ---")
    least_common_multiple(4, 6)
    least_common_multiple(15, 20)
    least_common_multiple(7, 13)

    print("\n--- Tests for (c) ---")
    arithmetic_progression(5, 2, 3)
    arithmetic_progression(10, 0, 5)
    arithmetic_progression(4, 10, -2)

    print("\n--- Tests for (d) ---")
    quadratic_roots(1, -5, 6)
    quadratic_roots(1, -4, 4)
    quadratic_roots(1, 1, 5)

    print("\n--- Tests for (e) ---")
    vector_statistics([1.5, 2.5, 3.5, 2.5, 5.0])
    vector_statistics([10, 20, 30, 40, 50, 30])
    vector_statistics([0.1, 0.1, 0.9, 0.5])

    print("\n--- Tests for (f) ---")
    vector_intersection([1, 2, 3, 4], [3, 4, 5, 6])
    vector_intersection([10, 20], [30, 40])
    vector_intersection([5, 5, 1], [5, 2])

    print("\n--- Tests for (g) ---")
    vector_union([1, 2, 3], [3, 4, 5])
    vector_union([10, 10], [20, 20])
    vector_union([], [1, 2])