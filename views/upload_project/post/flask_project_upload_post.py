from flask import Blueprint, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'images/'  # 업로드할 위치의 절대 경로

bp = Blueprint('flask_project_upload_post', __name__, url_prefix='/uploadPage')

@bp.route('/post', methods=['POST'])
def main_page():
    projectName = request.form['projectName']
    projectOneLineIntroduction = request.form['projectOneLineIntroduction']
    projectIntroduction = request.form['projectIntroduction']
    imagesFiles = request.files.getlist('projectImages')
    email = request.form['email']
    password = request.form['password']

    # 이미지 파일 저장
    for file in imagesFiles:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

    print(projectName)
    print(os.getcwd())
    return 'hi'
