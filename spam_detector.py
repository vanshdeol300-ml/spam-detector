from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Features: [links, capitals, exclamation, length]
X = np.array([
    [10, 1, 5, 200],
    [1, 0, 1, 50],
    [8, 1, 4, 180],
    [0, 0, 0, 30],
    [9, 1, 6, 220],
    [2, 0, 1, 60],
    [7, 1, 3, 150]
])

y = [1, 0, 1, 0, 1, 0, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

print("=== Spam Detector ===")
links = int(input("Kitne links hain? "))
capitals = int(input("Capital letters hain? (1/0) "))
exclamation = int(input("Kitne exclamation hain? "))
length = int(input("Email ki length? "))

result = model.predict([[links, capitals, exclamation, length]])

if result[0] == 1:
    print("SPAM hai!")
else:
    print("Spam nahi hai!")
