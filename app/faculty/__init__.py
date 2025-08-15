from flask import Blueprint

faculty = Blueprint('faculty', __name__, template_folder='templates')

from . import routes  # Import routes at the end to avoid circular imports
