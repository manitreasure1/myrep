from flask_nova import FlaskNova
from .menu import   menu_bp


def regester_routes(app: FlaskNova):
    app.register_blueprint(menu_bp, url_prefix="menu")