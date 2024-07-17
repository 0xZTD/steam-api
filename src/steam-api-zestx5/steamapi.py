from dotenv import load_dotenv
import os

import requests

load_dotenv()
# https://steamcommunity.com/dev/apikey
STEAM_KEY = os.getenv("STEAM_KEY")


def get_news_for_app(app_id: str, count: int, max_length: int, format: str = "json"):
    """Returns the lastest of a game specified by its appid

    Args:
        appid (str): AppID of the game you want the news of.
        count (int): How many news enties you want to get returned.
        maxlength (int): Maximum length of each news entry.
        format (str): Output format. json (default), xml or vdf.
    """
    URL = f"http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={app_id}&count={count}&maxlength={max_length}&format={format}"
    response = requests.get(URL)
    return response.text


if __name__ == "__main__":
    print(get_news_for_app("440", 3, 300))
