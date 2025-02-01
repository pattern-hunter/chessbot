import requests

def get_user_games_from_lichess(username, since):
    url = f"https://lichess.org/api/games/user/{username}?since={since}"
    response = requests.get(url)
    with open("games.txt", "w") as f:
        f.write(response.text)
        
get_user_games_from_lichess("pattern_hunter", 1736959353)