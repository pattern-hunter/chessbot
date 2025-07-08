from temporalio import workflow
from datetime import timedelta
from temporalio.common import RetryPolicy
from dataclasses import dataclass

with workflow.unsafe.imports_passed_through():
    import workflows_py.activities.random_forest.generate_data_activity as gda

@dataclass
class HyperparameterTuningWorkflowInput:
    test_size: float
    random_state: int

@workflow.defn
class HyperparameterTuningWorkflow:
    @workflow.run
    async def run(self, input: HyperparameterTuningWorkflowInput) -> str:
        (X_train, y_train) = await workflow.execute_activity(
            gda.generate_train_and_test_data,
            gda.GenerateDataInput(test_size=input.test_size, random_state=input.random_state, filename="~/Programming/chessbot/dataset.csv"),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        return (X_train, y_train)