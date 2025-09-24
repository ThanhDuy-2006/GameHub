class GameReview:
    def __init__(
        self,
        id: int,
        game_id: int,
        player_id: int,
        rating: int,
        comment: str | None = None,
        review_date=None,
    ):
        self.id = id
        self.game_id = game_id
        self.player_id = player_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date

    def __repr__(self):
        return f"<GameReview id={self.id}, game_id={self.game_id}, player_id={self.player_id}, rating={self.rating}>"
