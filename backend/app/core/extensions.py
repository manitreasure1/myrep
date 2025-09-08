from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from ext.sqlmodel import FlaskSQLModel


cors = CORS()
bcrypt =Bcrypt()
migrate = Migrate()
sqlmodel = FlaskSQLModel()

