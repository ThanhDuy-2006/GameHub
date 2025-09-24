from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.user_controller import bp as user_bp
from src.api.controllers.designer_controller import bp as designer_bp
from src.api.controllers.developer_controller import bp as developer_bp
from src.api.controllers.asset_purchases_controller import bp as asset_purchases_bp
from src.api.controllers.asset_controller import bp as asset_bp
from src.api.controllers.apiaccess_controller import bp as apiaccess_bp
from src.api.controllers.leaderboard_controller import bp as leaderboard_bp
from src.api.controllers.payout_transactions_controller import bp as payout_transactions_bp
from src.api.controllers.admin_controller import bp as admin_bp 
from src.api.controllers.game_review_controller import bp as game_review_bp
from src.api.controllers.game_controller import bp as game_bp
from src.api.controllers.player_controller import bp as player_bp
from src.api.controllers.reward_controller import bp as reward_bp
from src.api.controllers.redeem_controller import bp as redeem_bp



def register_routes(app):
    app.register_blueprint(todo_bp) 
    app.register_blueprint(user_bp)
    app.register_blueprint(designer_bp)
    app.register_blueprint(developer_bp)
    app.register_blueprint(asset_purchases_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(apiaccess_bp)
    app.register_blueprint(leaderboard_bp)
    app.register_blueprint(payout_transactions_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(game_review_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(reward_bp)
    app.register_blueprint(redeem_bp)
