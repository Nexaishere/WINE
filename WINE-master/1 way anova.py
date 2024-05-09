1 way Anova

import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

group1 = [23, 25, 29, 34, 30]
group2 = [19, 20, 22, 25, 24]
group3 = [15, 18, 20, 21, 17]
group4 = [28, 24, 26, 30, 29]

all_data = group1 + group2 + group3 + group4

group_labels = ['Group1'] * len(group1) + ['Group2'] * len(group2) + ['Group3'] * len(group3) + ['Group4'] * len(group4)

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)

# Print ANOVA results
print("One-way ANOVA:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Perform Tukey-Kramer post-hoc test
tukey_results = pairwise_tukeyhsd(all_data, group_labels)

# Print Tukey-Kramer results
print("\nTukey-Kramer post-hoc test:")
print(tukey_results)
