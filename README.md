# Spearman's_Permutation_Correlation_Test
A robust permutation test for testing the hypothesis H0: ρs = 0 based on an appropriately studentized statistic was developed by Han Yu and Alan D. Hutson in 2024 [1]. The script, `Spearmans_Permutation_Correlation_Test.py` calculates Spearman's Rank Correlation Coefficient and approximate p-values for the correlation between two variables based on ranked data based on the method and the formulas in the study conducted by Han Yu and Alan D. Hutson in 2024 [1]. It processes data from a CSV file and provides an easy-to-use interface for researchers and data scientists.
## How to Use
1. Prepare the CSV file and ensure your CSV file has two columns of numeric data (without headers). The script will calculate the correlation between the values in these two columns.
2. Update the File Path
3. Run the script
## Referencs
1. Yu, H., Hutson, A.D., 2024. A robust spearman correlation coefficient permutation test. Communications in Statistics-Theory and Methods 53, 2141–2153 (https://doi.org/10.1080/03610926.2022.2121144).

```bash
python Spearmans_Permutation_Correlation_Test.py
