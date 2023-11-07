from flask import Blueprint, render_template

bp = Blueprint('flask_project_upload', __name__, url_prefix='/uploadPage')

# main page
@bp.route('/')
def main_page() :
    return render_template('uploadPage.html')