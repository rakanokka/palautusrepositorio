import unittest
from player import Player
from statistics_service import SortBy, StatisticsService

class PlayerReaderStub:
    
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]
    

class StatisticsServiceTest(unittest.TestCase):
    
    def setUp(self):
        self.service = StatisticsService(PlayerReaderStub())

    def test_search_player(self):
        player = self.service.search("Semenko")
        self.assertIsNotNone(player) 
        self.assertEqual(player.name, "Semenko")

        player = self.service.search("Crosby")
        self.assertIsNone(player)

    def test_search_team(self):
        players = self.service.team("PIT")
        self.assertEqual(1, len(players))
        self.assertEqual(players[0].team, "PIT")
        
        players = self.service.team("EDM")
        self.assertEqual(3, len(players))
        self.assertEqual(players[0].team, "EDM")
        self.assertEqual(players[1].team, "EDM")
        self.assertEqual(players[2].team, "EDM")
        
        players = self.service.team("NJ")
        self.assertListEqual(players, [])

    def test_search_top_scorers(self):
        
        def assert_player_points(player: Player, name: str, points: int):
            self.assertEqual(player.name, name)
            self.assertEqual(player.goals + player.assists, points)
        
        top3 = self.service.top(3)
        self.assertEqual(3, len(top3))
        assert_player_points(top3[0], "Gretzky", 124)
        assert_player_points(top3[1], "Lemieux", 99)
        assert_player_points(top3[2], "Yzerman", 98)

        top5 = self.service.top(5)
        self.assertEqual(5, len(top5))
        assert_player_points(top5[0], "Gretzky", 124)
        assert_player_points(top5[1], "Lemieux", 99)
        assert_player_points(top5[2], "Yzerman", 98)
        assert_player_points(top5[3], "Kurri", 90)
        assert_player_points(top5[4], "Semenko", 16)

        empty = self.service.top(0)
        self.assertListEqual(empty, [])
    
    def test_search_top_goal_scorers(self):
        
        def assert_player_goals(player: Player, name: str, goals: int):
            self.assertEqual(player.name, name)
            self.assertEqual(player.goals, goals)
        
        top3 = self.service.top(3, SortBy.GOALS)
        self.assertEqual(3, len(top3))
        assert_player_goals(top3[0], "Lemieux", 45)
        assert_player_goals(top3[1], "Yzerman", 42)
        assert_player_goals(top3[2], "Kurri", 37)

        top5 = self.service.top(5, SortBy.GOALS)
        self.assertEqual(5, len(top5))
        assert_player_goals(top5[0], "Lemieux", 45)
        assert_player_goals(top5[1], "Yzerman", 42)
        assert_player_goals(top5[2], "Kurri", 37)
        assert_player_goals(top5[3], "Gretzky", 35)
        assert_player_goals(top5[4], "Semenko", 4)

        empty = self.service.top(0, SortBy.GOALS)
        self.assertListEqual(empty, [])

    def test_search_top_assist_leaders(self):
        
        def assert_player_assists(player: Player, name: str, assists: int):
            self.assertEqual(player.name, name)
            self.assertEqual(player.assists, assists)
        
        top3 = self.service.top(3, SortBy.ASSISTS)
        self.assertEqual(3, len(top3))
        assert_player_assists(top3[0], "Gretzky", 89)
        assert_player_assists(top3[1], "Yzerman", 56)
        assert_player_assists(top3[2], "Lemieux", 54)

        top5 = self.service.top(5, SortBy.ASSISTS)
        self.assertEqual(5, len(top5))
        assert_player_assists(top5[0], "Gretzky", 89)
        assert_player_assists(top5[1], "Yzerman", 56)
        assert_player_assists(top5[2], "Lemieux", 54)
        assert_player_assists(top5[3], "Kurri", 53)
        assert_player_assists(top5[4], "Semenko", 12)

        empty = self.service.top(0, SortBy.ASSISTS)
        self.assertListEqual(empty, [])
