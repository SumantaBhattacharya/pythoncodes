def add_polynomials(poly1, poly2):
    result = []

    # Pad the smaller polynomial with zeros to make them of equal length
    if len(poly1) < len(poly2):
        poly1 += [0] * (len(poly2) - len(poly1))
    else:
        poly2 += [0] * (len(poly1) - len(poly2))

    # Add corresponding coefficients
    for coeff1, coeff2 in zip(poly1, poly2):
        result.append(coeff1 + coeff2)

    return result

# Example polynomials
poly1 = [0, 5, 0, 10, 6]  # Represents 5^1 + 10x^2 + 6x^3
poly2 = [1, 2, 3]         # Represents 1 + 2x^1 + 3x^2

# Adding polynomials
result = add_polynomials(poly1, poly2)

# Output
print("Result of (5^1 + 10x^2 + 6x^3) + (1 + 2x^1 + 3x^2):", result)
