from flask import Blueprint

website = Blueprint('website', __name__)

from app.website import routes