def validate_queens(positions):
    for i in range(8):
        for j in range(i+1, 8):
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True