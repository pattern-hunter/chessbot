from temporalio import activity
from dataclasses import dataclass
from random_forest import *

@dataclass
class MLActivitiesInput:
    data_file: str
    model_file: str

@activity.defn(name="Training Activity")
async def training_activity(input: MLActivitiesInput) -> str:
    return train_random_forest(input.data_file)

@activity.defn(name="Testing Activity")
async def testing_activity(input: MLActivitiesInput) -> float:
    return show_model_accuracy(input.data_file, input.model_file)