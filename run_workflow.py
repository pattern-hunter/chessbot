import asyncio
from workflows_py.continuous_training_workflow import *
from workflows_py.activities.compose_greeting_activity import *
from temporalio.client import Client


async def main() -> None:

    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "World",
        id="hello-activity-workflow-id",
        task_queue="hello-activity-task-queue",
    )
    print(f"Result: {result}")



if __name__ == "__main__":
    asyncio.run(main())