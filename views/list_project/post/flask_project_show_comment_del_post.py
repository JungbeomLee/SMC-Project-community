from flask import Blueprint, request
from ...utils.mysql_connect import register_db
import bcrypt
import pymysql
import os

bp = Blueprint('flask_project_show_comment_del_post', __name__, url_prefix='/listPage/del')

@bp.route('/post', methods=['POST'])
def main_page():
    password = str(request.form['password'])
    postID = int(request.form['postID'])

    try:
        with register_db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("select password from project_post where project_post_id = %s", (postID))
            check_post = cursor.fetchone()

            if check_post :
                check_password = bcrypt.checkpw(password.encode('utf-8'), check_post['password'])

                if check_password :
                    cursor.execute("delete from project_post where project_post_id = %s", (postID))
                    register_db.commit()

                    cursor.execute("delete from project_post_comment where project_post_id = %s", (postID))
                    register_db.commit()

                    image_list = os.listdir('./static/db_images')
                    for image_name in image_list :
                        print(image_name[0], postID)
                        print(type(image_name[0]), type(postID))
                        if image_name[0] == str(postID) :
                            print(image_name)
                            print('hio')
                            os.remove('./static/db_images/'+image_name)

                    return {'STATUS': True}
                else :
                    return {'STATUS': False}
            return {'STATUS': False}
    except Exception as e:
        # Convert the exception to string
        error_message = str(e)
        print(e)
        return {'STATUS': False, 'ERROR': error_message}

