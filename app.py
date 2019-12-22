from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import index

from mod_users import users
from mod_admin import admin
from mod_blog import blog

app.register_blueprint(users)
app.register_blueprint(admin)
app.register_blueprint(blog)



if __name__ == '__main__':
    app.run()
