#@Ryu_god

import requests


API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM1NDMwMzdmLTBjODMtNDBkNC1iNGVhLTE4YjA0ZTU2ZGUwNyIsImlhdCI6MTY4MDMzMjE4OCwic3ViIjoiZGV2ZWxvcGVyLzJmYmVmZGJmLTg2MWUtY2RlOS0wY2M2LTE1ZGMwNjZhMDYxNSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEzNy45Ny43OC41MSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.t64BgE-XsZM3nBHm7qXogQ8Q4hcHPemALYlyM8CLbaw6cC671iEHnZd40KRyCDXe7jLEAC6BKSaodUh5NKclDg"
MY_TAG = "#LP2Q8PJPR"

headers = {"authorization": "Bearer " + API_TOKEN, "Accept": "application/json"}


class Player:
    def __init__(
        self, tag, name, clan, townhall_level, experience_level, trophies
    ) -> None:
        self.tag = tag
        self.name = name
        self.clan = clan
        self.townhall_level = townhall_level
        self.experience_level = experience_level
        self.trophies = trophies

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Player):
            raise Exception("Not a Player")

        return self.tag == __o.tag and self.tag == __o.tag


class Clan:
    def __init__(self, tag, name, level, points, total_members, members) -> None:
        self.tag = tag
        self.name = name
        self.level = level
        self.points = points
        self.total_members = total_members
        self.members = members

    def get_members(self):
        return self.members

    def find_player(self, player_tag):
        if player_tag in self.members:
            return self.members[player_tag]

    # max capacity
    def is_full(self):
        return self.total_members >= 50

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Player):
            raise Exception("Not a Clan")

        return self.tag == __o.tag and self.tag == __o.tag


class Manager:
    def __init__(self, all_players, all_clans) -> None:
        self.all_players = {}
        self.all_clans = {}

    def add_player(self, player_tag):
        if player_tag in self.all_players:
            raise Exception("Player already exists!")

        try:
            response = requests.get(
                "https://api.clashofclans.com/v1/players/%23" + player_tag,
                headers=headers,
            )
            data = response.json()
            player = Player(
                data["tag"],
                data["name"],
                data["clan"],
                data["expLevel"],
                data["trophies"],
            )
            self.all_players[player_tag] = player

        except requests.exceptions.HTTPError as errh:
            return ("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            return ("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            return ("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            return ("OOps: Something Else", err)

    def add_clan(self, clan_tag):
        if clan_tag in self.all_clans:
            raise Exception("Clan already exists!")

        try:
            response = requests.get(
                "https://api.clashofclans.com/v1/clans/%23" + clan_tag,
                headers=headers,
            )
            data = response.json()
            clan = Clan(
                data["tag"],
                data["name"],
                data["clanLevel"],
                data["clanPoints"],
                data["members"],
                data["memberList"],
            )
            self.all_clans.append(clan)

        except requests.exceptions.HTTPError as errh:
            return ("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            return ("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            return ("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            return ("OOps: Something Else", err)

    def sort_players_levels(self):
        self.all_players.sort(key=lambda p: p.levels)

    def sort_players_names(self):
        self.all_players.sort(key=lambda p: p.name)

    def sort_players_townhall(self):
        self.all_players.sort(key=lambda p: p.trophies)

    def sort_players_names(self):
        self.all_players.sort(key=lambda p: p.name)

    def find_player_tag(self, player_tag):
        if player_tag in self.all_players:
            return self.all_players[player_tag]
        else:
            raise Exception("Player does not exist!")

    def find_clan_tag(self, clan_tag):
        if clan_tag in self.all_clans:
            return self.all_clans[clan_tag]
        else:
            raise Exception("Clan does not exist!")
