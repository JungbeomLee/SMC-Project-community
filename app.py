from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the blueprint from the 'views.flask_main' module
    from views.flask_main import bp as flask_main_bp
    from views.upload_project.flask_project_upload import bp as flask_project_upload
    from views.upload_project.post.flask_project_upload_post import bp as flask_project_upload_post

    # Register the blueprint
    app.register_blueprint(flask_main_bp)
    app.register_blueprint(flask_project_upload)
    app.register_blueprint(flask_project_upload_post)

    # Run the application
    app.run(host='0.0.0.0', port=8000, debug=True)

# Run the application factory function
if __name__ == '__main__':
    create_app()
