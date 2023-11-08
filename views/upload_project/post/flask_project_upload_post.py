from flask import Blueprint, request
from werkzeug.utils import secure_filename
from ...utils.env_val import database_pwd
import pymysql
import bcrypt
import os

UPLOAD_FOLDER = 'images/'  # 업로드할 위치의 절대 경로

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
        # connect mysql DataBase
        register_db = pymysql.connect(
            host=   "localhost",
            user=   "root", 
            passwd= database_pwd, 
            db=     "smc_project_community_db", 
            charset="utf8"
        )
        cursor = register_db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT project_post_id FROM project_post order by project_post_id desc")
        post_id = cursor.fetchall()

        if not post_id : 
            post_id = 1
        else :
            post_id = post_id[0]

        # 이미지 파일 저장
        filename_list = []
        for index, file in enumerate(imagesFiles):
            filename = secure_filename(str(post_id)+str(index)+email+password+'.png')
            filename_list.append(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        
        filename_str = ''
        if len(filename_list) >= 2 :
            for i, filename in enumerate(filename_list) :
                filename_str += filename
                if len(filename_list) - (i+1) != 0 :
                    filename_str += ','
        else :
            filename_str = filename_list[0]

        try : 
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
            register_db.close()

            reps = {'STATUS' : True}

            return reps
        except Exception as e :
            reps = {'STATUS' : False, 'ERROR' : e}
            return reps

    except Exception as e :
        reps = {'STATUS' : False, 'ERROR' : e}
        return reps