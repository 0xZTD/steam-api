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


def get_global_achievement_percentages_for_app(game_id: str, format: str = "json"):
    """Returns on global achievements overview of a specific game in percentages.

    Args:
        game_id (str): AppID of the game you want the news of.
        format (str, optional): Output format. json (default), xml or vdf.
    """
    URL = f"http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={game_id}&format={format}"
    response = requests.get(URL)
    return response.text


def get_player_summaries(steam_ids: list[str], format: str = "json"):
    """Returns basic profile information for a list of 64-bit Steam IDs.

    Args:
        steamd_ids (list[str]): List of 64 bit Steam IDs to return profile information for. Up to 100 Steam IDs can be requested.
        format (str, optional): Output format. json (default), xml or vdf.
    """
    URL = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_KEY}&steamids={",".join(steam_ids)}"
    response = requests.get(URL)
    return response.text

def get_friend_list(steam_id:str,relationship:str,format:str = "json"):
    """Returns the friend list of any Steam user, provided their Steam Community profile visibility is set to "Public". 

    Args:
        steam_id (str): 64 bit Steam ID to return friend list for.
        relationship (str): Relationship filter. Possibles values: all, friend.
        format (str, optional): Output format. json (default), xml or vdf. 
    """
    URL = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={STEAM_KEY}&steamid={steam_id}&relationship={relationship}"
    response = requests.get(URL)
    return response.text

def get_player_achievements(steam_id:str,app_id:str,lang:str=""):
    """Returns a list of achievements for this user by app id 

    Args:
        steam_id (str): 64 bit Steam ID to return friend list for.
        app_id (str): The ID for the game you're requesting
        lang (str, optional): Language. If specified, it will return language data for the requested language.
    """
    if lang == "":
        URL = f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={app_id}&key={STEAM_KEY}&steamid={steam_id}"
    else:
        URL = f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={app_id}&key={STEAM_KEY}&steamid={steam_id}&l={lang}"
    
    response = requests.get(URL) 
    return response.text

if __name__ == "__main__":
    # print(get_news_for_app("440", 3, 300))
    # print(get_global_achievement_percentages_for_app("440"))
    # print(get_player_summaries(["76561199170929376","76561197960435530"]))
    # print(get_friend_list("76561197960435530","all"))
    # print(get_player_achievements("76561199170929376","2379780","Russian"))
    pass
