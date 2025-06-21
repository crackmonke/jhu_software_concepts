from flask import Flask

from board import pages

# Factory function to create and configure the Flask app
def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    # Register the pages blueprint with the app
    app.register_blueprint(pages.bp)
    return app