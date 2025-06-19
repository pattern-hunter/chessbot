from temporalio import activity
from dataclasses import dataclass
from parse import parse_data

@dataclass
class FileIOActivityInput:
    data: str
    filename: str

@activity.defn(name="Write Game Data To File")
async def write_game_data_to_file_activity(input: FileIOActivityInput) -> None:
    with open(input.filename, "w") as f:
        f.write(input.data)

@activity.defn(name="Parse Game Data")
async def parse_game_data_file_activity(input: FileIOActivityInput) -> str:
    data_filename = parse_data(input.filename)
    return data_filename