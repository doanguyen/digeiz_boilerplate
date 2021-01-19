from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy  # type: ignore

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
