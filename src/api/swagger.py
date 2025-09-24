from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from api.schemas.todo import TodoRequestSchema, TodoResponseSchema
from api.schemas.user import UserRequestSchema, UserResponseSchema
from api.schemas.player import PlayerRequestSchema, PlayerResponseSchema
from api.schemas.reward import RewardRequestSchema, RewardResponseSchema
from api.schemas.redeem import RedeemRequestSchema, RedeemResponseSchema
from api.schemas.developer import DeveloperRequestSchema, DeveloperResponseSchema
from api.schemas.asset_purchases import AssetPurchaseRequestSchema, AssetPurchaseResponseSchema
from api.schemas.asset import AssetRequestSchema, AssetResponseSchema
from api.schemas.designer import DesignerRequestSchema, DesignerResponseSchema
from api.schemas.apiaccess import ApiaccessRequestSchema, ApiaccessResponseSchema
from api.schemas.leaderboard import LeaderboardRequestSchema, LeaderboardResponseSchema
from api.schemas.payout_transactions import PayoutTransactionsRequestSchema, PayoutTransactionsResponseSchema
from api.schemas.admin import AdminRequestSchema, AdminResponseSchema   
from api.schemas.game import GameRequestSchema, GameResponseSchema
from api.schemas.game_review import GameReviewRequestSchema, GameReviewResponseSchema
spec = APISpec(
    title="Todo API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Đăng ký schema để tự động sinh model
spec.components.schema("TodoRequest", schema=TodoRequestSchema)
spec.components.schema("TodoResponse", schema=TodoResponseSchema)
spec.components.schema("UserRequest", schema=UserRequestSchema)
spec.components.schema("UserResponse", schema=UserResponseSchema)
spec.components.schema("PlayerRequest", schema=PlayerRequestSchema)
spec.components.schema("PlayerResponse", schema=PlayerResponseSchema)
spec.components.schema("RewardRequest", schema=RewardRequestSchema)
spec.components.schema("RewardResponse", schema=RewardResponseSchema)
spec.components.schema("RedeemRequest", schema=RedeemRequestSchema)
spec.components.schema("RedeemResponse", schema=RedeemResponseSchema)
spec.components.schema("DesignerRequest", schema=DesignerRequestSchema)
spec.components.schema("DesignerResponse", schema=DesignerResponseSchema)
spec.components.schema("DeveloperRequest", schema=DeveloperRequestSchema)
spec.components.schema("DeveloperResponse", schema=DeveloperResponseSchema)
spec.components.schema("AssetPurchaseRequest", schema=AssetPurchaseRequestSchema)
spec.components.schema("AssetPurchaseResponse", schema=AssetPurchaseResponseSchema)
spec.components.schema("AssetRequest", schema=AssetRequestSchema)
spec.components.schema("AssetResponse", schema=AssetResponseSchema)
spec.components.schema("ApiaccessRequest", schema=ApiaccessRequestSchema)
spec.components.schema("ApiaccessResponse", schema=ApiaccessResponseSchema)
spec.components.schema("LeaderboardRequest", schema=LeaderboardRequestSchema)
spec.components.schema("LeaderboardResponse", schema=LeaderboardResponseSchema)
spec.components.schema("PayoutTransactionsRequest", schema=PayoutTransactionsRequestSchema)
spec.components.schema("PayoutTransactionResponse", schema=PayoutTransactionsResponseSchema)
spec.components.schema("AdminRequest", schema=AdminRequestSchema)
spec.components.schema("AdminResponse", schema=AdminResponseSchema)
spec.components.schema("GameRequest", schema=GameRequestSchema)
spec.components.schema("GameResponse", schema=GameResponseSchema)
spec.components.schema("GameReviewRequest", schema=GameReviewRequestSchema)
spec.components.schema("GameReviewResponse", schema=GameReviewResponseSchema)
