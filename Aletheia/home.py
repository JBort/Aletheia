from flask import render_template, Blueprint, url_for

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    return render_template('/home.html')
