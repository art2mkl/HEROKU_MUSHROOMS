# import and register blueprints
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates' )

# import any flask extension specific to this module

# import views
from app.main import main_views