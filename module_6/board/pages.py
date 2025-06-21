"""Defines routes for the main pages of the website."""

from flask import Blueprint, render_template

# Create a Blueprint for page routes
bp = Blueprint("pages", __name__)

# Route for the home page
@bp.route("/")
def home():
    """Render the home page."""
    return render_template("pages/home.html", current_page="home")

# Route for the contact page
@bp.route("/contact")
def contact():
    """Render the contact page."""
    return render_template("pages/contact.html", current_page="contact")

# Route for the projects page
@bp.route("/projects")
def projects():
    """Render the projects page."""
    return render_template("pages/projects.html", current_page="projects")
