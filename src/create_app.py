from flask import Flask
from .config import Config
from .api.middleware import setup_middleware
from .api.routes import register_routes
from .infrastructure.databases import init_db
from .app_logging import setup_logging
from flask_jwt_extended import JWTManager
from cors import init_cors 

def create_app():
    app = Flask(__name__)
     # ✅ Bật CORS cho toàn bộ API
    init_cors(app)
    
    app.config.from_object(Config)

    jwt = JWTManager(app)
    setup_logging(app)
    init_db(app)
    setup_middleware(app)
    register_routes(app)

    return app