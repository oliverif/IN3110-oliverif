import os
import pathlib
import re
from typing import Dict, List
from urllib.parse import urljoin

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requesting_urls import get_html

## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()

base_url = "https://en.wikipedia.org"


def find_best_players(url: str) -> None:
    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    # gets the teams
    teams = get_teams(url)
    # assert len(teams) == 8

    # Gets the player for every team and stores in dict (get_players)
    all_players = {team["name"]: get_players(team["url"]) for team in teams}

    # get player statistics for each player,
    # using get_player_stats
    for team, players in all_players.items():
        for i in range(len(players)):
            all_players[team][i] = all_players[team][i] | get_player_stats(all_players[team][i]["url"], team)

    # at this point, we should have a dict of the form:

    # {
    #     "team name": [
    #         {
    #             "name": "player name",
    #             "url": "https://player_url",
    #             # added by get_player_stats
    #             "points": 5,
    #             "assists": 1.2,
    #             # ...,
    #         },
    #     ]
    # }

    # Select top 3 for each team by points:
    best = {}
    top_stat = "points"
    for team, players in all_players.items():
        # Sort and extract top 3 based on points
        sorted_players = sorted(players, key=lambda d: d[top_stat])
        top_3 = sorted_players[-3]
        top_2 = sorted_players[-2]
        top_1 = sorted_players[-1]
        best[team] = [top_1, top_2, top_3]

    stats_to_plot = ["points", "assists", "rebounds"]
    for stat in stats_to_plot:
        plot_best(best, stat=stat)


def plot_best(best: Dict[str, List[Dict]], stat: str = "points") -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """
    stats_dir = "NBA_player_statistics"
    try:
        os.mkdir(stats_dir)
    except FileExistsError:
        pass
    count_so_far = 0
    all_names = []

    # iterate through each team and the
    for team, players in best.items():
        # pick the color for the team, from the table above
        # color = color_table[team]
        # collect the points and name of each player on the team
        # you'll want to repeat with other stats as well
        points = []
        names = []
        for player in players:
            names.append(player["name"])
            points.append(player[stat])
        # record all the names, for use later in x label
        all_names.extend(names)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players points,
        # with the team name as the label
        bars = plt.bar(x, points, label=team)
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # add the legend with the colors  for each team
    plt.legend(loc=0)
    # turn off gridlines
    plt.grid(False)
    # set the title
    plt.title(f"{stat} per game")
    # save the figure to a file
    filename = pathlib.PosixPath(stats_dir + "/" + stat + ".png")
    print(f"Creating {filename}")
    plt.savefig(filename)
    plt.clf()
    return


def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")

    # lots of ways to do this,
    # but one way is to build a set of team names in the semifinal
    # and a dict of {team name: team url}

    team_links = {}  # dict of team name: team url
    in_semifinal = set()  # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")
        # useful for showing structure
        # print([c.get_text(strip=True) for c in cols])

        # TODO:
        # 1. if First Round column, record team link from `a` tag
        # 2. if semifinal column, record team name

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            in_semifinal.add(team_col.get_text(strip=True))

    # return list of dicts (there will be 8):
    # [
    #     {
    #         "name": "team name",
    #         "url": "https://team url",
    #     }
    # ]

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")

    # Get the table
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Roster").find_next("table")

    players = []
    # Loop over every row and get the names from roster
    rows = table.find_next("table").find_next("tbody").find_all("tr")[1:]

    for row in rows:
        # Get the columns
        cols = row.find_all("td")
        # find name links (a tags)
        a = cols[2].find("a")
        # and add to players a dict with
        players.append({"name": a.text.strip(), "url": "https://en.wikipedia.org" + a["href"]})

    # return list of players

    return players


def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    # Get the table with stats
    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Regular_season")
    table = table.find_next("table") if table is not None else soup.find(id="NBA").find_next("table")
    all_rows = table.tbody.find_all("tr")

    labels = stat_inds = [c.text.strip() for c in all_rows[0].find_all("th")]

    team_col = labels.index("Team")
    year_col = labels.index("Year")
    stat_dict = {"RPG": "rebounds", "APG": "assists", "PPG": "points"}
    stat_inds = [labels.index(w) for w in stat_dict.keys()]

    rows = all_rows[1:]

    stats = {key: 0 for key in stat_dict.values()}

    # Loop over rows and extract the stats
    for row in rows:
        cols = row.find_all("td")

        # Check correct team (some players change team within season)
        if cols[team_col].text.strip() == team and cols[year_col].text.strip().startswith("2021"):
            # load stats from columns
            # keys should be 'points', 'assists', etc.
            for stat_ind, stat_name in zip(stat_inds, stat_dict.values()):
                stats[stat_name] = float(cols[stat_ind].text.strip().rstrip("*"))

    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)
