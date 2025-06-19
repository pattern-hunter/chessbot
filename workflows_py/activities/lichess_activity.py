from temporalio import activity
from dataclasses import dataclass
import requests

@dataclass
class LichessActivityInput:
    username: str
    since: str

@activity.defn(name="Get Lichess Games For User")
async def get_lichess_games_for_user(input: LichessActivityInput) -> str:
    lichess_url = f"https://lichess.org/api/games/user/{input.username}?since={input.since}"
    response = requests.get(lichess_url)
    return response.text