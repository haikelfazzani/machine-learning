from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

dataset = pd.read_table("fromage.txt")

print(dataset)

# X = dataset.iloc[:, 3:-1].values
target = dataset.iloc[:, 0].values
#
# print(X)
print(target)
#
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X, target)
#
# # make predictions
# print(model.predict([[2200]]))
# print(model.predict([[220]]))
