from flask import Blueprint, request
from werkzeug.utils import secure_filename
from ...utils.mysql_connect import register_db
import bcrypt
import os
import pymysql

UPLOAD_FOLDER = 'static/db_images'  # 업로드할 위치의 절대 경로

bp = Blueprint('flask_project_upload_post', __name__, url_prefix='/uploadPage')

@bp.route('/post', methods=['POST'])
def main_page():
    projectName = request.form['projectName']
    projectOneLineIntroduction = request.form['projectOneLineIntroduction']
    projectIntroduction = request.form['projectIntroduction']
    imagesFiles = request.files.getlist('projectImages')
    projectLink = request.form.get('projectLink')  # Use .get for optional fields
    projectGithub = request.form.get('projectGithub')  # Use .get for optional fields
    userInstagram = request.form.get('userInstagram')  # Use .get for optional fields
    email = request.form['email']
    password = request.form['password']
    password = (bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())).decode('utf-8')

    try :
        with register_db.cursor(pymysql.cursors.DictCursor) as cursor :
            cursor.execute("SHOW TABLE STATUS LIKE 'project_post'")
            post_id = cursor.fetchone()
            post_id = post_id['Auto_increment']
            print(post_id)

        # 이미지 파일 저장
        filename_list = []
        for index, file in enumerate(imagesFiles):
            filename = secure_filename(str(post_id)+str(index)+email+password+'.png')
            filename_list.append(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        
        filename_str = ''
        for filename in filename_list :
            filename_str += filename
            filename_str += ','

        try : 

            with register_db.cursor(pymysql.cursors.DictCursor) as cursor :
                sql = '''
                    INSERT INTO project_post (
                        project_title,
                        project_image_name,
                        project_OneLine_info,
                        project_info,
                        project_link,
                        github,
                        user_insta,
                        user_email,
                        password
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(sql, (
                    projectName,
                    filename_str,
                    projectOneLineIntroduction,
                    projectIntroduction,
                    projectLink if projectLink else None,  # 값이 없으면 None으로 설정
                    projectGithub if projectGithub else None,  # 값이 없으면 None으로 설정
                    userInstagram if userInstagram else None,  # 값이 없으면 None으로 설정
                    email,
                    password
                ))
                register_db.commit()

            reps = {'STATUS' : True}

            return reps
        except Exception as e :
            error_message = str(e)
            print(e)
            reps = {'STATUS' : False, 'ERROR' : e}
            return reps

    except Exception as e :
        error_message = str(e)
        print(e)
        reps = {'STATUS' : False, 'ERROR' : e}
        return reps