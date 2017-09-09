from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.models import  User, Profile

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

@manager.command
def initdb():
    db.create_all()

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()