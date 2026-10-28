import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../defect-logs/defect-summary.csv")
data = data.sort_values("Count", ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(data["Category"], data["Count"])
plt.xlabel("Defect Category")
plt.ylabel("Number of Defects")
plt.title("Defect Counts by Category")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig("defect-summary-chart.png", dpi=150)
