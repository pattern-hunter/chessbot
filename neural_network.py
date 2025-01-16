from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import csv
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

def conv_ascii(s):
	result = ""
	for c in s:
		result += str(ord(c))
	return result

# Initialize the MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42, solver='adam')

with open("dataset.csv", "r") as datafile:
	X, y = [], []
	csvlines = list(csv.DictReader(datafile))

	classesinit = False

	for i in range(100):
		np.random.shuffle(csvlines)
		for line in csvlines:
			X.append([conv_ascii(line["opponent"])])
			y.append(line["index"])

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
		scaler = StandardScaler()
		X_train = scaler.fit_transform(X_train)
		X_test = scaler.transform(X_test)

		if not classesinit:
			classes = np.unique(y)
			classesinit = True

		# Train the model
		mlp.partial_fit(X_train, y_train, classes=classes)

		y_pred = mlp.predict(X_test)

		print(f"Accuracy {i+1}:", accuracy_score(y_test, y_pred))
		# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
		# print("Classification Report:\n", classification_report(y_test, y_pred))