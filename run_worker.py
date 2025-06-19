# import sys
# from parse import parse_data

# function_name = sys.argv[1]

# if function_name == "parse":
#     filename = sys.argv[2]
#     parse_data(filename)

import asyncio
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from workflows_py.continuous_training_workflow import *
from workflows_py.activities.lichess_activity import *
from workflows_py.activities.file_io_activities import *
from workflows_py.activities.ml_activities import *

from temporalio.client import Client
from temporalio.worker import Worker


# While we could use multiple parameters in the activity, Temporal strongly
# encourages using a single dataclass instead which can have fields added to it
# in a backwards-compatible way.



async def main():
    # Uncomment the lines below to see logging output
    # import logging
    # logging.basicConfig(level=logging.INFO)

    # Start client
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="ml-queue",
        workflows=[ContinuousTrainingWorkflow],
        activities=[
            get_lichess_games_for_user,
            write_game_data_to_file_activity,
            parse_game_data_file_activity,
            training_activity,
            testing_activity
        ],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())