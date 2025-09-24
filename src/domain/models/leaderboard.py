class Leaderboard:
    def __init__(self, id: int, player_id: int, game_id: int, score: int, achieved_at):
        self.id = id
        self.player_id = player_id
        self.game_id = game_id
        self.score = score
        self.achieved_at = achieved_at