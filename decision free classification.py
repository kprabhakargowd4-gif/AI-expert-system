# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the model
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Display Results
print("\n🌸 Decision Tree Structure:")
print(export_text(clf, feature_names=iris.feature_names))

print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
