from flask import Blueprint, request
from ...utils.mysql_connect import register_db
import bcrypt
import pymysql

bp = Blueprint('flask_project_show_comment_post', __name__, url_prefix='/listPage')

@bp.route('/post', methods=['POST'])
def main_page():
    commentName = request.form['commentName']
    commentPassword = request.form['commentPassword']
    commentPassword = (bcrypt.hashpw(commentPassword.encode('UTF-8'), bcrypt.gensalt())).decode('utf-8')
    commentInput = request.form['commentInput']
    postID = int(request.form['postID'])

    try:
        with register_db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                INSERT INTO project_post_comment 
                (
                project_post_id, 
                user_name, 
                password,
                comment_text
                ) VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (postID, commentName, commentPassword, commentInput))
            register_db.commit()

        return {'STATUS': True}
    except Exception as e:
        # Convert the exception to string
        error_message = str(e)
        print(e)
        return {'STATUS': False, 'ERROR': error_message}

