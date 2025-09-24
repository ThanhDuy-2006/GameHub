from infrastructure.databases.mssql import init_mssql
from infrastructure.models import (
    todo_model, 
    user_model, 
    player_model, 
    developer_model, 
    designer_model,
    admin_model, 
    reward_model,
    redeem_model,
    game_model, 
    game_review_model, 
    leaderboard_model,
    asset_model,
    asset_purchases_model,
    apiaccess_model,
    payout_transactions_model,
    )

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base