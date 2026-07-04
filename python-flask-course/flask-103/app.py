from flask import Flask
from config import Config
from routes import routes
from models import db

# Flask app creating
app = Flask(__name__)

# Load the configuration from the Config class inside the application
app.config.from_object(Config)

# Initialize the database with the Flask app
db.init_app(app)
# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Import the routes function from the routes package
routes(app)

if __name__ == "__main__":
    app.run(debug=True) 