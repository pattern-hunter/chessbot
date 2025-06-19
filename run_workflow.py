import asyncio
from workflows_py.continuous_training_workflow import *
from temporalio.client import Client


async def main() -> None:

    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        ContinuousTrainingWorkflow.run,
        ContinuousTrainingWorkflowInput(username="punmaster_general", since="1736959353"),
        id="continuous-training-workflow",
        task_queue="ml-queue"
    )
    print(f"Result: {result}")



if __name__ == "__main__":
    asyncio.run(main())