from enum import Enum

class SortBy(Enum):
    GOALS = 1
    ASSISTS = 2
    POINTS = 3

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, by = SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by(player):
            if by == SortBy.GOALS:
                return player.goals
            if by == SortBy.ASSISTS:
                return player.assists
            return player.points


        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
