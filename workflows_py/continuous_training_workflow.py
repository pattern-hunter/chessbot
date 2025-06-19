from temporalio import workflow
from datetime import timedelta
from temporalio.common import RetryPolicy
from dataclasses import dataclass

with workflow.unsafe.imports_passed_through():
    import workflows_py.activities.lichess_activity as la
    import workflows_py.activities.file_io_activities as fwa
    import workflows_py.activities.ml_activities as ml

@dataclass
class ContinuousTrainingWorkflowInput:
    username: str
    since: str

# Basic workflow that logs and invokes an activity
@workflow.defn
class ContinuousTrainingWorkflow:
    @workflow.run
    async def run(self, input: ContinuousTrainingWorkflowInput) -> str:
        games_data = await workflow.execute_activity(
            la.get_lichess_games_for_user,
            la.LichessActivityInput(username=input.username, since=input.since),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        await workflow.execute_activity(
            fwa.write_game_data_to_file_activity,
            fwa.FileIOActivityInput(data=games_data, filename="games_data.txt"),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        dataset_filename = await workflow.execute_activity(
            fwa.parse_game_data_file_activity,
            fwa.FileIOActivityInput(data="", filename="games_data.txt"),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        model_filename = await workflow.execute_activity(
            ml.training_activity,
            ml.MLActivitiesInput(data_file=dataset_filename, model_file=""),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        accuracy = await workflow.execute_activity(
            ml.testing_activity,
            ml.MLActivitiesInput(data_file=dataset_filename, model_file=model_filename),
            start_to_close_timeout=timedelta(seconds=600),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )

        return accuracy