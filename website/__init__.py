from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the SQLAlchemy extension
db = SQLAlchemy()
DB_NAME = "database.db"

# Create a global app variable
app = None

def create_app():
    global app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import your blueprints here (e.g., views and auth)
    from .views import views
    from .auth import auth

    # Register the blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    create_database(app)
    
    # Import your User model (adjust the import path as needed)
    from .models import User, Comment, Post, Like

    # Create the database tables within the application context
    with app.app_context():
        db.create_all()

    # Initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/"+DB_NAME):
        with app.app_context():
            db.create_all()
        print("Creating database!")

# Call create_app and assign the result to app
app = create_app()
