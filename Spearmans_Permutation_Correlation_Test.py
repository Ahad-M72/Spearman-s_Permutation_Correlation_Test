import csv
import random
from math import sqrt

def read_csv(filepath):
    with open(filepath, newline='') as csvfile:
        datareader = csv.reader(csvfile)
        headers = next(datareader)
        data = {h: [] for h in headers}
        for row in datareader:
            for h, val in zip(headers, row):
                data[h].append(float(val))
    return data




def spearman_rank_correlation(x, y):
    n = len(x)
    
# (i) calculate the ranks

    rank_x = [sorted(x).index(v) + 1 for v in x]
    rank_y = [sorted(y).index(v) + 1 for v in y]




# (ii) calculate spaerman's correlation (r_s)

    d_squared = sum((rx - ry) ** 2 for rx, ry in zip(rank_x, rank_y))
    return 1 - (6 * d_squared) / (n * (n**2 - 1))

def calculate_moments(x, y):
    n = len(x)
    rank_x = [sorted(x).index(v) + 1 for v in x]
    rank_y = [sorted(y).index(v) + 1 for v in y]
    avg_x = sum(rank_x) / n
    avg_y = sum(rank_y) / n
    mu_20 = sum((rx - avg_x)**2 for rx in rank_x) / n
    mu_02 = sum((ry - avg_y)**2 for ry in rank_y) / n
    mu_22 = sum((rx - avg_x)**2 * (ry - avg_y)**2 for rx, ry in zip(rank_x, rank_y)) / n
    return mu_22, mu_20, mu_02





# (iii) estimate the variance of sample estimates (tau_n_squared)

def calculate_variance(mu_22, mu_20, mu_02):
    return mu_22 / (mu_20 * mu_02)




# (iv) calculate the studentized statistic (R_s)


def permute_test(x, y, B=1000):
    rs = spearman_rank_correlation(x, y)
    mu_22, mu_20, mu_02 = calculate_moments(x, y)
    tau_n_squared = calculate_variance(mu_22, mu_20, mu_02)
    tau_n = sqrt(tau_n_squared)
    R_s = rs / tau_n
    R_s_permutations = []




# (v) calculate the studentized statistic for each permutation (R_s_permutations) 
    for _ in range(B):
        random.shuffle(y)  # Permute y in-place
        rs_perm = spearman_rank_correlation(x, y)
        R_s_permutations.append(rs_perm / tau_n)


    
# (vi) calculate the p-value

    p_value = sum(1 for R_perm in R_s_permutations if abs(R_perm) > abs(R_s)) / B
    return rs, p_value

def main():
    file_path = 'path/to/your/file.csv'
    data = read_csv(file_path)
    rs, p_value = permute_test(data['Column_name_1'], data['Column_name_2'])
    
    print(f"Spearman's Rank Correlation Coefficient: {rs}")
    print(f"P-value from permutation test: {p_value}")
    
    # (vii) Decision

    alpha = 0.05  # Set your significance level
    if p_value <= alpha:
        print("Reject the null hypothesis.")
    else:
        print("Fail to reject the null hypothesis.")
    
    

if __name__ == "__main__":
    main()
