from flask import Blueprint, render_template
from ..utils.mysql_connect import register_db
import pymysql
import bcrypt
import os

bp = Blueprint('flask_project_list', __name__, url_prefix='/listPage')

# main page
@bp.route('/')
def main_page() :
    with register_db.cursor(pymysql.cursors.DictCursor) as cursor :
        cursor.execute("SELECT project_title, project_image_name, project_OneLine_info, user_email FROM project_post")
        post_list = cursor.fetchall()
        
    return render_template('listPage.html', post_list = post_list)