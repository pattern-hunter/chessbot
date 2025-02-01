from temporalio import activity
from workflows.params import lichess_params
import json, requests, re
from pathlib import Path
import sqlite3 as sql
import base64, random
import datetime, os
import os
from time import sleep

@activity.defn(name="lichess_get_games_for_username_activity")
async def lichess_get_games_for_username_activity(input: lichess_params.LichessParams) -> str:
    print("before url")
    url = f"https://lichess.org/api/games/user/{input.username}?since={input.since}"
    print(f"After url: {url}")
    response = requests.get(url)
    with open("games.txt", "w") as f:
        f.write(response.text)