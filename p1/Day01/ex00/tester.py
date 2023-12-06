from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

try:
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))

    limit = 26
    result = apply_limit(bmi, limit)
    print(result)

except ValueError as e:
    print(f"Error: {e}")
