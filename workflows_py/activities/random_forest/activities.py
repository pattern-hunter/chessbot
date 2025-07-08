from temporalio import activity
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import csv

@dataclass
class GenerateDataInput:
    test_size: float
    random_state: int
    filename: str
    
@dataclass
class ModelData:
    X: list
    y: list

@dataclass
class ModelFitInput:
    max_estimators: int
    depth: int
    training_data: ModelData
    testing_data: ModelData

def conv_ascii(s):
	result = ""
	for c in s:
		result += str(ord(c))
	return result

@activity.defn(name="RF: Generate Train and Test Data")
async def generate_train_and_test_data(input: GenerateDataInput) -> tuple:
    with open(input.filename, "r") as datafile:
        X, y = [], []
        csvlines = list(csv.DictReader(datafile))

        for line in csvlines:
            X.append([conv_ascii(line["opponent"])])
            y.append(line["mine"])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=input.test_size, random_state=input.random_state)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        return (X_train, y_train, X_test, y_test)


@activity.defn(name="RF: Fit model and check accuracy")
async def fit_model_and_check_accuracy(input: ModelFitInput) -> float:
    best_accuracy = -1.0
    for i in range(1, input.max_estimators+1):
        rf = RandomForestClassifier(n_estimators=i, max_depth=input.depth)
        rf.fit(input.training_data.X, input.training_data.y)
        y_pred = rf.predict(input.testing_data.X)
        accuracy = accuracy_score(input.testing_data.y, y_pred)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
    
    return best_accuracy