from temporalio import activity
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import csv

@dataclass
class GenerateDataInput:
    test_size: float
    random_state: int
    filename: str

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
        return (X_train, y_train)