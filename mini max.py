def minimax(depth, node, is_max, values):
    if depth == 2:
        return values[node]

    if is_max:
        return max(
            minimax(depth + 1, node * 2, False, values),
            minimax(depth + 1, node * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, values),
            minimax(depth + 1, node * 2 + 1, True, values)
        )

# -------- INPUT --------
values = list(map(int, input("Enter leaf node values: ").split()))

result = minimax(0, 0, True, values)
print("Optimal value:", result)
