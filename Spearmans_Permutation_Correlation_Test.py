def read_csv(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    
    # Process rows to extract numbers
    data = [line.strip().split(',') for line in data[1:]]  # Skip header
    return [(float(row[0]), float(row[1])) for row in data]

def rank(data):
    sorted_data = sorted((e, i) for i, e in enumerate(data))
    ranks = [0] * len(data)
    curr_rank = 1
    # Handle ties by assigning the average rank
    for i in range(len(sorted_data)):
        if i > 0 and sorted_data[i][0] == sorted_data[i-1][0]:
            curr_rank -= 1
            avg_rank = (curr_rank + i + 1) / 2.0
            ranks[sorted_data[i-1][1]] = avg_rank
            ranks[sorted_data[i][1]] = avg_rank
        else:
            ranks[sorted_data[i][1]] = i + 1
        curr_rank += 1
    return ranks

def calculate_spearman(filepath):
    data = read_csv(filepath)
    column_a, column_b = zip(*data)  # Unpack data into separate columns

    ranks_a = rank(column_a)
    ranks_b = rank(column_b)

    d_squared_sum = sum((r_a - r_b) ** 2 for r_a, r_b in zip(ranks_a, ranks_b))
    n = len(column_a)
    spearman_corr = 1 - (6 * d_squared_sum) / (n * (n ** 2 - 1))

    return spearman_corr

# Adjust file path accordingly
file_path = 'path/to/your/file.csv'
result = calculate_spearman(file_path)
print(f"Spearman's correlation coefficient is: {result:.4f}")
import math

def calculate_spearman_p_value(r_s, n):
    # Calculate the t-statistic from Spearman's rho
    if r_s == 1 or r_s == -1:
        return 0  # Perfect correlation, p-value will be effectively 0
    t_statistic = r_s * math.sqrt((n - 2) / (1 - r_s**2))
    
    # Approximate the p-value using Z-distribution (for large n, > 30)
    # This is a simplification and may not be accurate for smaller sample sizes
    z = abs(t_statistic)  # Convert t to standard normal variable
    # Approximate the area under the curve beyond z for a two-tailed test
    if z < 1.645:
        return "greater than 0.1 (not significant)"
    elif z < 1.96:
        return "between 0.05 and 0.1 (marginally significant)"
    elif z < 2.576:
        return "less than 0.01 (significant)"
    else:
        return "less than 0.001 (highly significant)"

# Example usage
file_path = 'path/to/your/file.csv'
r_s = calculate_spearman(file_path)
n = 50  # Sample size
p_value_approx = calculate_spearman_p_value(r_s, n)
print(f"Approximate p-value range is: {p_value_approx}")
