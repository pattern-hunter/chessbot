from temporalio import workflow
from datetime import timedelta
from temporalio.common import RetryPolicy
from dataclasses import dataclass

with workflow.unsafe.imports_passed_through():
    import workflows_py.activities.random_forest.activities as rfa

@dataclass
class HyperparameterTuningWorkflowInput:
    test_size: float
    random_state: int
    max_depth: int
    max_estimators: int

@workflow.defn
class HyperparameterTuningWorkflow:
    @workflow.run
    async def run(self, input: HyperparameterTuningWorkflowInput) -> str:
        (X_train, y_train, X_test, y_test) = await workflow.execute_activity(
            rfa.generate_train_and_test_data,
            rfa.GenerateDataInput(test_size=input.test_size, random_state=input.random_state, filename="dataset.csv"),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        best_accuracy = -1
        for i in range(1, input.max_depth+1):
            accuracy = await workflow.execute_activity(
                rfa.fit_model_and_check_accuracy,
                rfa.ModelFitInput(max_estimators=input.max_estimators, depth=i, training_data=rfa.ModelData(X=X_train, y=y_train), testing_data=rfa.ModelData(X=X_test, y=y_test)),
                start_to_close_timeout=timedelta(seconds=600),
                retry_policy=RetryPolicy(maximum_attempts=3)
            )
            if accuracy > best_accuracy:
                best_accuracy = accuracy

        return best_accuracy