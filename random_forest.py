from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import csv
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import helpers
from random import randint
from sklearn.model_selection import RandomizedSearchCV
import pickle

# https://www.datacamp.com/tutorial/random-forests-classifier-python

def train_random_forest(filename):
	with open(filename, "r") as datafile:
		X, y = [], []
		csvlines = list(csv.DictReader(datafile))

		for line in csvlines:
			X.append([helpers.conv_ascii(line["opponent"])])
			y.append(line["mine"])

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
		scaler = StandardScaler()
		X_train = scaler.fit_transform(X_train)
		X_test = scaler.transform(X_test)

		rf = RandomForestClassifier(n_estimators=43, max_depth=19)
		rf.fit(X_train, y_train)
		with open("model.pkl", "wb") as pklfile:
			pickle.dump(rf, pklfile)
	return "model.pkl"
	

	# param_dist = {'n_estimators': list(range(1, 101)), 'max_depth': list(range(1, 21))}
	# # print(f"Params distribution: {param_dist}")
	# # rf = RandomForestClassifier()
	# for n in range(1, 101):
	# 	for d in range(1, 21):
	# 		rf = RandomForestClassifier(n_estimators=n, max_depth=d)
	# 		rf.fit(X_train, y_train)
	# 		y_pred = rf.predict(X_test)
	# 		accuracy = accuracy_score(y_test, y_pred)
	# 		print(f"Accuracy for n={n}, d={d}: {accuracy}")
	

	# rand_search = RandomizedSearchCV(
	# 	rf,
	# 	param_distributions = param_dist, 
    #     n_iter=5, 
    #     cv=5
    # )
	# rand_search.fit(X_train, y_train)
	# best_rf = rand_search.best_estimator_
	
	# # Print the best hyperparameters
	# print('Best hyperparameters:',  rand_search.best_params_)
	# best_rf.fit(X_train, y_train)
	# y_pred = best_rf.predict(X_test)
	# accuracy = accuracy_score(y_test, y_pred)
	# print("Accuracy:", accuracy)
    
	