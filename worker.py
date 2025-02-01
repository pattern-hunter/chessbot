import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflows import continuous_training_workflow
from workflows.activities import lichess_activity

# Queue workflow from Python: https://docs.temporal.io/develop/python/temporal-clients

# temporal workflow start \
#   --task-queue lichess-queue \
#   --type ContinuousLearningWorkflow \
#   --workflow-id 123 \
#   --input 'punmaster_general' 1736959353

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="lichess-queue",
        workflows=[continuous_training_workflow.ContinuousLearningWorkflow],
        activities=[lichess_activity.lichess_get_games_for_username_activity],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())