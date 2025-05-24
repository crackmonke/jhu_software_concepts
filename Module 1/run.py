# Import the create_app function from the board module
from board import create_app

# Create an instance of the Flask application
app = create_app()

# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)