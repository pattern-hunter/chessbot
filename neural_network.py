from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import csv
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import helpers

layers = []
for i in range(10, 101):
	for j in range(10, 101):
		for k in range(10, 101):
			layers.append((i, j, k))

hyperparameter_space = {
    'hidden_layer_sizes': layers,
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5],
    'learning_rate': ['constant','adaptive'],
}

classesinit = False

with open("dataset.csv", "r") as datafile:
	X, y = [], []
	csvlines = list(csv.DictReader(datafile))

	for line in csvlines:
		X.append([helpers.conv_ascii(line["opponent"])])
		y.append(line["index"])

	if not classesinit:
		classes = np.unique(y)
		classesinit = True

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
	scaler = StandardScaler()
	X_train = scaler.fit_transform(X_train)
	X_test = scaler.transform(X_test)

	# Initialize the MLPClassifier
	mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=10000, random_state=42, solver='adam')
	clf = GridSearchCV(mlp, hyperparameter_space, n_jobs=-1, cv=5)
	clf.fit(X_train, y_train) # X is train samples and y is the corresponding labels
	print('Best parameters found:\n', clf.best_params_)

	# mlp = MLPClassifier(
	# 	activation='tanh',
	# 	alpha=0.0001,
	# 	learning_rate='constant',
	# 	hidden_layer_sizes=(10, 30, 10),
	# 	max_iter=1000,
	# 	solver='sgd'
	# )


	# mlp.partial_fit(X_train, y_train, classes)
	# y_pred = mlp.predict(X_test)
	# print(f"Accuracy: ", accuracy_score(y_test, y_pred))

	# classesinit = False

	# for i in range(100):
	# 	np.random.shuffle(csvlines)
	# 	for line in csvlines:
	# 		X.append([conv_ascii(line["opponent"])])
	# 		y.append(line["index"])

	# 	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
	# 	scaler = StandardScaler()
	# 	X_train = scaler.fit_transform(X_train)
	# 	X_test = scaler.transform(X_test)

	# 	if not classesinit:
	# 		classes = np.unique(y)
	# 		classesinit = True

	# 	# Train the model
	# 	mlp.partial_fit(X_train, y_train, classes=classes)

	# 	y_pred = mlp.predict(X_test)

	# 	print(f"Accuracy {i+1}:", accuracy_score(y_test, y_pred))
		# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
		# print("Classification Report:\n", classification_report(y_test, y_pred))