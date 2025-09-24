class Redeem:
    def __init__(self, id: int, player_id: int, reward_id: int, points_used: int, status: str, created_at):
        self.id = id
        self.player_id = player_id
        self.reward_id = reward_id
        self.points_used = points_used
        self.status = status
        self.created_at = created_at