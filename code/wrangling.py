import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load .csv file
data = pd.read_csv("data/forest_health_data.csv")
print(data.head()) # Thanks Ziya @ Kaggle for the dataset!

##################################

# Main question we want to answer with this dataset: which variables are related to tree health status?

# Sub-questions:
# Is _______ related to health tree status?
    # a) tree height?
    # b) elevation?
    # c) soil metrics?
    # d) disturbance level?
    # e) fire risk index?

# Hypothesis: d and e will be more related.

#################################

# Let's first visualize the probably correlated variables as boxplots:

# 1. Tree height
sns.boxplot(x="Health_Status", y="Tree_Height", data=data, hue="Health_Status")
plt.xlabel("Health status")
plt.ylabel("Tree health")
plt.show()

# 2. Elevation
sns.boxplot(x="Health_Status", y="Elevation", data=data, hue="Health_Status")
plt.xlabel("Health status")
plt.ylabel("Elevation")
plt.show()

# 3. Soil metrics


# 4. Disturbance level
sns.boxplot(x="Health_Status", y="Disturbance_Level", data=data, hue="Health_Status")
plt.xlabel("Health status")
plt.ylabel("Disturbance level")
plt.show()

# 5. Fire risk index
sns.boxplot(x="Health_Status", y="Fire_Risk_Index", data=data, hue="Health_Status")
plt.xlabel("Health status")
plt.ylabel("Fire risk index")
plt.show()