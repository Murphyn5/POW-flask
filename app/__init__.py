import os
from flask import Flask, render_template, request, session, redirect, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from .models import db, User
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.article_routes import article_routes
from .api.article_image_routes import article_image_routes
from .api.community_event_routes import community_event_routes
from .api.community_event_image_routes import community_event_image_routes
from .api.documentary_image_routes import documentary_image_routes
from .api.documentary_routes import documentary_routes
from .api.meeting_routes import meeting_routes
from .api.meeting_image_routes import meeting_image_routes
from .api.noap_routes import noap_routes
from .seeds import seed_commands
from .config import Config


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands/
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(article_routes, url_prefix='/api/articles')
app.register_blueprint(article_image_routes, url_prefix='/api/article_images')
app.register_blueprint(community_event_routes, url_prefix='/api/community_events')
app.register_blueprint(community_event_image_routes, url_prefix='/api/community_event_images')
app.register_blueprint(documentary_image_routes, url_prefix='/api/documentary_images')
app.register_blueprint(documentary_routes, url_prefix='/api/documentaries')
app.register_blueprint(meeting_routes, url_prefix='/api/meetings')
app.register_blueprint(meeting_image_routes, url_prefix='/api/meeting_images')
app.register_blueprint(noap_routes, url_prefix='/api/noaps')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

# @app.route('/api/get_csrf_token', methods=['GET'])
# def get_csrf_token():
#     csrf_token = generate_csrf()
#     response = make_response(jsonify({'csrf_token': csrf_token}))
#     response.headers['Set-Cookie'] = f'csrf_token={csrf_token}; Secure; HttpOnly; SameSite=Strict'
#     return response


@app.before_request
def https_redirect():
    if os.environ.get('FLASK_DEBUG') == 1:
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_DEBUG') == 1 else False,
        samesite='Strict' if os.environ.get(
            'FLASK_DEBUG') == 1 else None,
        httponly=True)
    return response
