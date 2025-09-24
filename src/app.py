from flask import Flask, jsonify
from api.swagger import spec
from api.controllers.todo_controller import bp as todo_bp
from api.controllers.user_controller import bp as user_bp
from api.controllers.player_controller import bp as player_bp
from api.controllers.reward_controller import bp as reward_bp
from api.controllers.redeem_controller import bp as redeem_bp
from api.controllers.designer_controller import bp as designer_bp
from api.controllers.developer_controller import bp as developer_bp
from api.controllers.asset_purchases_controller import bp as asset_purchases_bp
from api.controllers.asset_controller import bp as asset_bp
from api.controllers.apiaccess_controller import bp as apiaccess_bp
from api.controllers.leaderboard_controller import bp as leaderboard_bp
from api.controllers.payout_transactions_controller import bp as payout_transactions_bp
from api.controllers.admin_controller import bp as admin_bp
from api.controllers.game_controller import bp as game_bp
from api.controllers.game_review_controller import bp as game_review_bp
from api.middleware import middleware
from api.responses import success_response
from infrastructure.databases import init_db
from config import Config
from flasgger import Swagger
from config import SwaggerConfig
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    Swagger(app)
    # Set JWT secret key (use your .env or config value)
    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
    jwt = JWTManager(app)
    # Đăng ký blueprint trước
    app.register_blueprint(todo_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(reward_bp)
    app.register_blueprint(redeem_bp)
    app.register_blueprint(designer_bp)
    app.register_blueprint(developer_bp)
    app.register_blueprint(asset_purchases_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(apiaccess_bp)
    app.register_blueprint(leaderboard_bp)
    app.register_blueprint(payout_transactions_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(game_review_bp)
    
     # Thêm Swagger UI blueprint
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Todo API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    try:
        init_db(app)
    except Exception as e:
        print(f"Error initializing database: {e}")

    # Register middleware
    middleware(app)

    # Register routes
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            # Thêm các endpoint khác nếu cần
            if rule.endpoint.startswith(('todo.', 'course.', 'user.', 'player.', 'reward.', 'redeem.', 'designer.', 'developer.', 'asset_purchases.', 'apiaccess.', 'asset.', 'leaderboard.', 'payout_transactions.', 'admin.', 'game.', 'game_review.')):
                view_func = app.view_functions[rule.endpoint]
                print(f"Adding path: {rule.rule} -> {view_func}")
                spec.path(view=view_func)

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
        return response


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)