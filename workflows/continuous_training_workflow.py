from temporalio import workflow, activity
from workflows.params import lichess_params
from datetime import timedelta
from dataclasses import dataclass
from temporalio.client import Client
from temporalio.worker import Worker
import asyncio
from datetime import datetime

with workflow.unsafe.imports_passed_through():
    from workflows.activities import lichess_activity

@workflow.defn(name="ContinuousLearningWorkflow")
class ContinuousLearningWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        print("Running")
        return await workflow.execute_activity(
                lichess_activity.lichess_get_games_for_username_activity,
                lichess_params.LichessParams("punmaster_general", 1736959353),
                schedule_to_close_timeout=timedelta(seconds=10),
            )