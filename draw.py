import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# UDP no ethem
data = []
# print(len(data))
# mean and confidence interval
mean_value = np.mean(data)
confidence_interval = stats.norm.interval(0.95, loc=np.mean(data), scale=stats.sem(data))

# the data
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

#  data points
sns.barplot(x=np.arange(len(data)), y=data, color='skyblue', errorbar= None)

#  the mean 
plt.axhline(y=mean_value, color='red', linestyle='--', label='Mean')
print("Mean value: {:.3f}".format(mean_value))

# Plot the confidence interval as error bars
plt.errorbar(x=len(data) / 2, y=mean_value, yerr=np.diff(confidence_interval) / 2,
             color='black', linewidth=2, capsize=5, label='95% CI')
plt.ylim(0.245, 0.270)

# Set labels and title
plt.xlabel('Experiment Number')
plt.ylabel('Times')
plt.title('Mean and Confidence Intervals of UDP - no ethem')
plt.legend()


plt.show()