from flask import Blueprint, render_template, request
from ..utils.mysql_connect import register_db
import pymysql
import bcrypt
import os

bp = Blueprint('flask_project_show', __name__, url_prefix='/listPage')

@bp.route('/<select_board_number>')
def main_page() :
    with register_db.cursor(pymysql.cursors.DictCursor) as cursor :

    return render_template('listPage.html')
