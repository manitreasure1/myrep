from flask_nova import NovaBlueprint
from core.extensions import sqlmodel

menu_bp = NovaBlueprint("menu", __name__)


def get_db():
    return sqlmodel.session()

