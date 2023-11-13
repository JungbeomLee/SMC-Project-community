from flask import Blueprint, render_template, request
from ..utils.mysql_connect import register_db
import pymysql
import bcrypt
import os

bp = Blueprint('flask_project_show', __name__, url_prefix='/listPage')

@bp.route('/<select_board_number>')
def main_page(select_board_number):
    try:
        select_board_number = int(select_board_number)  # 정수 변환을 확인
        with register_db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM project_post WHERE project_post_id = %s", (select_board_number,))
            post_list = cursor.fetchall()

        return render_template('postShowPage.html', post_list=post_list)
    except Exception as e:
        # 오류 로깅 및 처리
        print(f"An error occurred: {e}")
        # 적절한 오류 응답 반환

    