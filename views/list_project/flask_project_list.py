from flask import Blueprint, render_template, request
from ..utils.mysql_connect import register_db
import pymysql
import bcrypt
import os

bp = Blueprint('flask_project_list', __name__, url_prefix='/listPage')

@bp.route('/')
def main_page() :
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    
    per_page = 15   
    with register_db.cursor(pymysql.cursors.DictCursor) as cursor :
        # 검색어에 따른 전체 게시글 수 계산
        if search_query:
            search_query = f"%{search_query}%"
            cursor.execute("SELECT COUNT(*) FROM project_post WHERE project_title LIKE %s", (search_query,))
            total_posts = cursor.fetchone()['COUNT(*)']
        else:
            cursor.execute("SELECT COUNT(*) FROM project_post")
            total_posts = cursor.fetchone()['COUNT(*)']

        total_pages = (total_posts + per_page - 1) // per_page

        # 검색어가 있을 경우 해당 검색어를 포함하는 데이터 검색
        if search_query:
            cursor.execute("SELECT project_post_id, datetime, project_title, project_image_name, project_OneLine_info, user_email FROM project_post WHERE project_title LIKE %s LIMIT %s OFFSET %s", (search_query, per_page, (page-1)*per_page))
        else:
            # 검색어가 없을 경우 모든 데이터 반환
            cursor.execute("SELECT project_post_id, datetime, project_title, project_image_name, project_OneLine_info, user_email FROM project_post LIMIT %s OFFSET %s", (per_page, (page-1)*per_page))

        post_list = cursor.fetchall()

    return render_template('listPage.html', post_list=post_list, total_pages=total_pages, current_page=page)
