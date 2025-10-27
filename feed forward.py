# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Feed-Forward Neural Network
# 1 hidden layer with 5 neurons, 'relu' activation
model = MLPClassifier(hidden_layer_sizes=(5,), activation='relu', max_iter=1000, random_state=1)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Display results
print("✅ Feed-Forward Neural Network Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Predicted:", y_pred)
print("Actual:", y_test)
