import random

# Stările
states = ["A", "B", "C", "D"]

# Matricea de tranziție (Markov)
P = [
    [0.00, 0.50, 0.50, 0.00],
    [0.33, 0.00, 0.33, 0.33],
    [0.00, 1.00, 0.00, 0.00],
    [0.00, 0.00, 1.00, 0.00]
]

# alegere stare următoare pe baza probabilităților
def next_state(current_index):
    r = random.random()
    cumulative = 0

    for j, prob in enumerate(P[current_index]):
        cumulative += prob
        if r <= cumulative:
            return j

    return len(P[current_index]) - 1


# simulare Markov
def simulate(start, steps):
    path = [states[start]]
    current = start

    for _ in range(steps):
        current = next_state(current)
        path.append(states[current])

    return path


# rulare
result = simulate(start=0, steps=10)
print(" -> ".join(result))