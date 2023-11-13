from flask import Blueprint, render_template, request
from ..utils.mysql_connect import register_db
import pymysql
import bcrypt
import os

bp = Blueprint('flask_project_show', __name__, url_prefix='/listPage')

@bp.route('/<select_board_number>')
def main_page(select_board_number) :
    with register_db.cursor(pymysql.cursors.DictCursor) as cursor :
        cursor.execute("SELECT * FROM project_post WHERE project_post_id = %s", (select_board_number))
        post_list = cursor.fetchall()

    register_db.close()

    return render_template('postShowPage.html', post_list = post_list)
