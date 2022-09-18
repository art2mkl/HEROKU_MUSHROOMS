# import and register blueprints
from flask import Blueprint

architecture = Blueprint('architecture', __name__, template_folder='templates' )

# import views
from app.architecture import architecture_views