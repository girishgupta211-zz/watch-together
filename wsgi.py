from flask_migrate import Migrate

from watch_together.app import db, app as application

migrate = Migrate(application, db)
