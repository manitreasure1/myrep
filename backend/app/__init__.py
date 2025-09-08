from flask_nova import FlaskNova
from .routers import regester_routes
from .config.env_config import EnvConfig
from .core.extensions import *

env_config = EnvConfig() # type: ignore

def create_app(config_object="config.Development"):
    app = FlaskNova(__name__)
    app.config.from_object(env_config)
    bcrypt.init_app(app)
    migrate.init_app(app)
    sqlmodel.init_app(app)
    cors.init_app(
        app,
        resources={
            r"/api/*": {"origins": "*"}
            }, 
            allow_headers=['Content-Type', 'Authorization'],
            methods=['GET', 'POST', 'PUT', 'DELETE'],
            max_age=3600
            )

    regester_routes(app)
    return app