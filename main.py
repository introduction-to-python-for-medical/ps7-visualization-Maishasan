import matplotlip.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='diabetes', version=1, as_frame=True)
df = data.frame
features = list(df.columns)
selected_features = [features[0], features[2], features[1], features[5], features[4]]
fig, axs = plt.subplots(1, len(selected_features), figsize = (20,3))
for ax, f in zip(axs, selected_features):
  ax.hist(df[f], bins=5, color='pink', edgecolor='black')
  ax.set_xlapel(f)
reference_feature = selected_features[2]
y = df[reference_feature]
fig, axs = plt.subplots(1, len(features), figsize = (20,3))
for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)
plt.show()
reference_feature = selected_features[2]
comparison_features = selected_features[4]
plt.figure(figsize=(8,6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.8)
plt.xlapel(reference_feature)
plt.ylapel(comparison_features)
plt.savefig('correlation_plot.png')
plt.show()
